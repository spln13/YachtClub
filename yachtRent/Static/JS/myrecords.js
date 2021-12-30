returnYacht = (yachtid) => {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '/api/lease/returnyacht');
    const dataToSend = {"yachtid": yachtid};
    httpRequest.send(JSON.stringify(dataToSend));
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert("归还成功");
    }
    else {
        alert("归还失败");
    }
}

createBox = (yachtid, yachtname, time, flag) => {
    let mother_box = document.querySelector('.records');
    let box = document.createElement('tr');
    mother_box.appendChild(box);
    if (flag === 'y') {
        box.innerHTML ='<td>' + yachtid + '</td><td>' + yachtname + '</td><td>' + time + '</td><td>' + '已还</td>';
    }
    else {
        box.innerHTML = '<td>' + yachtid + '</td><td>' + yachtname +
                        '</td><td>' + time + '</td><td>' + '<a href="" id=' + yachtid + ' onclick="returnYacht(id)">点击归还</a></td>';
    }
}

window.onload = () => {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getusername', false);
    httpRequest.send();
    let strReceive = String(httpRequest.response);
    let response = JSON.parse(JSON.parse(strReceive));
    const username = response['username'];
    if (username === 0) {
        window.location.href = "/login/";
    }
    httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/yacht/getmyrentrecords', false)
    httpRequest.send()
    strReceive = String(httpRequest.response);
    const records = JSON.parse(JSON.parse(strReceive))
    for (let i = 0; i < records.length; i++) {
        createBox(records[i]['yachtid'], records[i]['yachtname'], records[i]['time'], records[i]['flag']);
    }

}
