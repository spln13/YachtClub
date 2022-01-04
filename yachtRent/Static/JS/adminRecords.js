const dump = () => {
    const httpRequest2 = new XMLHttpRequest();
    httpRequest2.open('GET', '/api/dump', false);
    httpRequest2.send();
    const strReceive2 = String(httpRequest2.response);
    const response2 = JSON.parse(JSON.parse(strReceive2));
    const code2 = response2['code'];
    if (code2 === 1) {
        alert('备份成功');
    } else {
        alert('备份失败');
    }
}

const logout = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/login/adminlogout', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert('登出成功');
        window.location.href = '/adminLogin/'
    } else {
        alert('登出失败');
    }
}

const createBox = (recordid, username, yachtid, yachtname, time, returnTime, flag) => {
    let mother_box = document.querySelector('.records');
    let box = document.createElement('tr');
    mother_box.appendChild(box);
    box.innerHTML = '<td>' + recordid + '</td><td>' + username + '</td><td>' + yachtid + '</td><td>' + yachtname +
        '</td><td>' + time + '</td><td>' + returnTime + '</td><td>' + flag + '</td>';
}

window.onload = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getadminname', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const adminname = response['adminname'];
    if (adminname !== 0) { // 登陆状态 修改右上角
        document.getElementById("adminname").innerHTML = '' + adminname;
    }
    const httpRequest1 = new XMLHttpRequest();
    httpRequest1.open('GET', '/api/yacht/getAllRecords', false);
    httpRequest1.send();
    const strReceive1 = String(httpRequest1.response);
    const records = JSON.parse(JSON.parse(strReceive1));
    for (let i = 0; i < records.length; i++) {
        if (!records[i]['returnTime']) {
            records[i]['returnTime'] = '未还';
        }
        records[i]['flag'] = records[i]['flag'] === 'y' ? '已还' : '未还';
        createBox(records[i]['recordid'], records[i]['username'], records[i]['yachtid'], records[i]['yachtname'],
            records[i]['time'], records[i]['returnTime'], records[i]['flag']);
    }
}