const logout = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/login/userlogout', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert('登出成功');
        window.location.href = '/home/'
    } else {
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
    console.log(username)
    if (username !== 0) { // 登陆状态 修改右上角
        let right = document.getElementById("right");
        console.log(right);
        right.innerHTML = '<li>' + username +'</li><button type="button" onclick="logout()" class="btn btn-warning">登出</button>'
    }
}