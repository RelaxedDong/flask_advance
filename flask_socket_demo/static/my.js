    var socket = io.connect('http://' + document.domain + ':' + location.port);
    function Mybtn() {
        socket.emit('json', {data: '快过年了哟，祝大家新年快乐~(管理员)', sender: 'admin', reciver: 'all_font_users'});

        socket.emit('return_json',{
            'username':'odnghao',
            'age':20,
            'place':'nyist'
        })
    }

    socket.on('response', function (foo,bar,data,ack) {
        var MessageDiv = document.getElementById('messages');
        MessageDiv.innerHTML = data
        ack('我收到了哈')
    });


     socket.on('return_json', function (data) {
        console.log(data)
    });