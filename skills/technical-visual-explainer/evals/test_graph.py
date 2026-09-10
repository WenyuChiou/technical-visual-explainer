import importlib.util
from pathlib import Path
import unittest

module_spec=importlib.util.spec_from_file_location('check_graph',Path(__file__).resolve().parents[1]/'scripts/check_graph.py')
module=importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


def valid_graph():
    nodes=[{'id':name,'role':'process','label':name} for name in ('input','work','check','fix','output','human')]
    nodes[-1]['label']='WAIT: researcher'
    return {'nodes':nodes,'edges':[
        {'source':'input','target':'work'}, {'source':'work','target':'check'},
        {'source':'check','target':'output','outcome':'PASS'},
        {'source':'check','target':'fix','outcome':'REVISE'},
        {'source':'fix','target':'work'},
        {'source':'check','target':'human','outcome':'HUMAN'}],
        'loops':[{'check':'check','work':'work','output':'output','human':'human'}]}


class GraphTests(unittest.TestCase):
    def test_closed_loop_and_wait(self):
        self.assertEqual(module.audit(valid_graph()),[])
    def test_record_bypass(self):
        g=valid_graph();g['nodes'].append({'id':'record','role':'record','label':'Saved record'})
        g['edges'] += [{'source':'fix','target':'record'},{'source':'record','target':'output'}]
        self.assertTrue(any('without PASS' in x for x in module.audit(g)))
    def test_dangling_human(self):
        g=valid_graph();g['nodes'][-1]['label']='Researcher'
        self.assertTrue(any('dead end' in x for x in module.audit(g)))
    def test_missing_revision_return(self):
        g=valid_graph();g['edges']=[e for e in g['edges'] if e['source']!='fix']
        self.assertTrue(any('return to rework' in x for x in module.audit(g)))
    def test_unknown_endpoint(self):
        g=valid_graph();g['edges'].append({'source':'missing','target':'check'})
        self.assertTrue(any('unknown endpoint' in x for x in module.audit(g)))
    def test_human_can_resume_into_rechecking(self):
        g=valid_graph();g['nodes'][-1]['label']='Researcher decides';g['edges'].append({'source':'human','target':'work'})
        self.assertEqual(module.audit(g),[])
    def test_human_cannot_bypass_check(self):
        g=valid_graph();g['edges'].append({'source':'human','target':'output'})
        self.assertTrue(any('without PASS' in x for x in module.audit(g)))
    def test_revision_cannot_skip_declared_work(self):
        g=valid_graph();g['edges'].append({'source':'fix','target':'check'})
        self.assertTrue(any('bypass declared rework' in x for x in module.audit(g)))
    def test_human_can_end_at_separate_wait_node(self):
        g=valid_graph();g['nodes'][-1]['label']='Clarify research scope'
        g['nodes'].append({'id':'wait','role':'researcher','label':'WAIT: researcher reply'})
        g['edges'].append({'source':'human','target':'wait'})
        self.assertEqual(module.audit(g),[])
    def test_stop_substring_is_not_terminal(self):
        g=valid_graph();g['nodes'][-1]['label']='Review stopwatch timings'
        self.assertTrue(any('dead end' in x for x in module.audit(g)))
    def test_human_dead_cycle_is_not_a_terminal(self):
        g=valid_graph();g['nodes'][-1]['label']='Clarify scope'
        g['edges'].append({'source':'human','target':'human'})
        self.assertTrue(any('waiting terminal' in x for x in module.audit(g)))


if __name__=='__main__': unittest.main()
