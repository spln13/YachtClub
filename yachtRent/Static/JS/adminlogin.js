
window.onload = () => {
    const btn_login = document.querySelector('#btn_login');
    const usn = document.querySelector('#username');
    const pwd = document.querySelector('#password');

    btn_login.addEventListener('click', function (e) {
        e.preventDefault();
        const username = usn.value;
        const password = pwd.value;
        if (username === '' || password === '') {
            alert('请输入信息');
            return null;
        }
        const dataToSend = {'adminname': username, 'adminpwd': password};
        const httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', '/api/login/adminverify',false);
        httpRequest.send(JSON.stringify(dataToSend));
        const strReceive = String(httpRequest.response);
        const response = JSON.parse(JSON.parse(strReceive));
        const code = response['code'];
        if (code === 0) {
            alert('登录成功');
            window.location.href = "/admin/";
            return null;
        }
        else if (code === 1) {
            alert('密码错误');
            return null;
        }
        else {
             alert('管理员不存在');
             return null;
        }
    })
}
