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

deleteUser = (username) => {
    const dataToSend = {"username": username};
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '/api/user/deleteuser');
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


createBox = (username, password, email) => {
    let mother_box = document.querySelector('.userinfo');
    let box = document.createElement('tr');
    mother_box.appendChild(box);
    box.innerHTML ='<td>' + username + '</td><td>' + password + '</td><td>' + email +
        '</td><td><a href="" id=' + username + ' onclick="deleteUser(id)">删除</a></td>';
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
    httpRequest1.open('GET', '/api/user/getalluser', false);
    httpRequest1.send();
    console.log(httpRequest1.response);
    const strReceive1 = String(httpRequest1.response);
    const userinfo = JSON.parse(JSON.parse(strReceive1));
    console.log(userinfo);
    for (let i = 0; i < userinfo.length; i++) {
        createBox(userinfo[i]["username"], userinfo[i]["password"], userinfo[i]["email"]);
    }
}