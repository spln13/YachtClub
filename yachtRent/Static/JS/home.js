logout = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/login/userlogout', false);
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

window.onload = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getusername', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const username = response['username'];  // 0: 未登录; username: 用户名
    if (username !== 0) { // 登陆状态 修改右上角
        document.getElementById("login").innerHTML = '<a href="">'+ username +'</a>'
        document.getElementById("signup").innerHTML = '<a href="" onclick="logout()">登出</a>'
    }
}