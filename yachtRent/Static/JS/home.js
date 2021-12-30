window.onload = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getusername', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const username = response['username'];  // 0: 未登录; username: 用户名
    if (username !== 0) { // 登陆状态 修改右上角
        document.getElementById("login").innerHTML = '<a href="">'+ username +'</a>'
        document.getElementById("signup").innerHTML = '<a href="/api/login/userlogout">登出</a>'
    }

}