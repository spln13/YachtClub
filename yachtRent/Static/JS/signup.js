const sendDataAjax = (dataToSend, url) => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', url, false);
    httpRequest.send(JSON.stringify(dataToSend));
    const strReceive = String(httpRequest.response);
    console.log(strReceive);
    return JSON.parse(JSON.parse(strReceive));
}

window.onload = () => {
    const btn_signin = document.querySelector('#btn_signin');
    const usn = document.querySelector('#username');
    const pwd1 = document.querySelector('#password1');
    const pwd2 = document.querySelector('#password2');
    const eml = document.querySelector('#email');
    const sex = document.getElementsByName('sex');
    btn_signin.addEventListener('click', function (e) {
        e.preventDefault();
        const username = usn.value;
        const password1 = pwd1.value;
        const password2 = pwd2.value;
        const email = eml.value;
        const ismale = sex[0].checked;
        if (username === '' || password1 === '' || password2 === '' || email === '' || ismale === '') {
            // 有信息没有输入完全
            alert('请输入完整信息');
            return null;
        }
        if (username.length > 25) {
            alert('请输入短一点的用户名');
            return null
        }
        const response = sendDataAjax({'username': username}, '/api/register/check_username');
        const isExist = response['isExist'];
        if (isExist === 1) {
            alert('用户名已存在');
            return null;
        }
        const reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
        const isEmailOk =reg.test(email);
        if (!isEmailOk) {
            alert('邮箱不合法');
            return null;
        }
        const noValid = ['.', ',', '@', '/', '{', '}', ';'];
        for (let i = 0; i < username.length; i++) {
            for (let j = 0; j < noValid.length; j++) {
                if (username[i] === noValid[j]) {
                    // error('用户名不合法');
                    alert('用户名含有特殊符号');
                    return null;
                }
            }
        }
        if (password1 !== password2) {
            alert('密码不一致');
            return null;
        }
        const dataToSend = {'username': username, 'password': password1, 'email': email, 'ismale': ismale};
        const httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', '/api/register/storage', false);
        httpRequest.send(JSON.stringify(dataToSend));
        const strReceive = String(httpRequest.response)
        const response2 = JSON.parse(JSON.parse(strReceive));
        const code = response2['code'];
        if (code === 1) {
            alert('注册成功');
            window.location.href = "/home/";
        }
        else {
            alert('注册失败');
        }
    })
}