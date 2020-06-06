
function AjaxSubmit_set() {
    var question_t = document.getElementById('chartinput').value
    var chatbox = document.getElementById('chartBox');
    var questionbox = document.createElement('div');
    questionbox.className = "chatout";
    var questiontext = document.createElement('span');
    questiontext.innerText = question_t;
    questionbox.appendChild(questiontext);
    chatbox.appendChild(questionbox);
    chatbox.scrollTop = chatbox.scrollHeight;
    $.ajax({
        url:'',
        type:'POST',
        // data:{data:JSON.stringify(question)},
        data:{
            'question':question_t
        },
        success: function (data) {
            var t1_text = data['node']
            var t2_text = data['rela']
            document.getElementById('chartinput').value = ''
            console.log(data['node'])
            console.log(t1_text)
            var chatbox = document.getElementById('chartBox');
            var questionbox = document.createElement('div');
            questionbox.className = "chatin";
            var questiontext = document.createElement('span');
            questiontext.innerText = data['answer'];
            questionbox.appendChild(questiontext);
            chatbox.appendChild(questionbox);
            chatbox.scrollTop = chatbox.scrollHeight;
            try {
                $("svg").remove()
                var data = {}
                data.nodes = JSON.parse(t1_text);
                data.links = JSON.parse(t2_text);
                var config = {
                    //鼠标mouseover后的弹窗
                    content:null,
                    contentHook: contentHook,
                    //节点配色方案（可为空)
                    nodeColor: null,
                    //连接线配色方案（可为空）
                    linkColor: null,
                    width: 1050,
                    height: 750
                }
                initKG(data, config, "#container")
            } catch (err) {
                Materialize.toast('渲染存在异常', 2000)
                console.info(err)}
            
        }
    })
}

