addYacht = () => {
    const yachtname = prompt('请输入要发布的游艇名');
    const num = prompt('请输入要发布的数量');
    const httpRequest = new XMLHttpRequest();
    const dataToSend = {"yachtname": yachtname, "num": num};
    httpRequest.open('POST', '/api/yacht/publish', false);
    httpRequest.send(JSON.stringify(dataToSend));
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert('添加成功');
    }
    else {
        alert('添加失败');
    }
}


logout = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/login/adminlogout', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert('登出成功');
    }
    else {
        alert('登出失败');
    }
}

deleteYacht = (yachtid) => {
    const dataToSend = {"yachtid": yachtid};
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '/api/yacht/delete');
    httpRequest.send(JSON.stringify(dataToSend));
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code']
    if (code === 1) {
        alert('删除成功');
    }
    else {
        alert('删除失败');
    }
}

createBox = (yachtid, yachtname) => {
    let mother_box = document.querySelector('.yachtinfo');
    let box = document.createElement('tr');
    mother_box.appendChild(box);
    box.innerHTML ='<td>' + yachtid + '</td><td>' + yachtname +
        '</td><td><a href="" id=' + yachtid + ' onclick="deleteYacht(id)">删除</a></td>';
}

window.onload =() => {
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
    httpRequest1.open('GET', '/api/yacht/query', false);
    httpRequest1.send();
    const strReceive1 = String(httpRequest1.response);
    const yachtinfo = JSON.parse(JSON.parse(strReceive1));
    console.log(yachtinfo);
    for (let i = 0; i < yachtinfo.length; i++) {
        createBox(yachtinfo[i]["yachtid"], yachtinfo[i]["yachtname"]);
    }
}