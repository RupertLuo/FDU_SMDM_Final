from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import sys
sys.path.append('/Users/luoruipu/dasanxia/社交网络挖掘/FDU_SMDM_Final')
from qc_lg.question_classification import Question_classify
from qc_lg.question_query import QuestionQuery
import json as js
@csrf_exempt
def home(request):
    if dict(request.POST) !={}:
        question = dict(request.POST)['question'][0]
        qc = Question_classify()
        q_index, entities = qc.predict(question)
        qa = QuestionQuery(q_index, entities)
        answer = qa.get_question_answer()
        graph = qa.GetSubgraph()
        node,rel = graph2json(graph)
        response = JsonResponse({'answer':answer,'node':js.dumps(node,ensure_ascii=False),'rela':js.dumps(rel,ensure_ascii=False)})
        return response
    return render(request,'visulization/home.html')

def graph2json(graph):
    nodelist = []
    nodetype = []
    rel = []
    for edge in graph:
        if 'person' in edge:
            if edge['person'] not in nodelist:
                nodelist.append(edge['person'])
                nodetype.append('person')
        if 'movie' in edge:
            if edge['movie'] not in nodelist:
                nodelist.append(edge['movie'])
                nodetype.append('movie')
        if 'type' in edge:
            if edge['type'] not in nodelist:
                nodelist.append(edge['type'])
                nodetype.append('type')

    node = {i:{'name':nodelist[i],'type':nodetype[i]} for i in range(len(nodelist))}
    for edge in graph:
        three_unit = {}
        if 'person' in edge and 'movie' in edge:
            three_unit['source'] = nodelist.index(edge['person'])
            three_unit['target'] = nodelist.index(edge['movie'])
        elif 'movie' in edge and 'type' in edge:
            three_unit['source'] = nodelist.index(edge['movie'])
            three_unit['target'] = nodelist.index(edge['type'])
        three_unit['rela'] = edge['rela']
        three_unit['type'] = edge['rela']
        rel.append(three_unit)
    return node,rel

