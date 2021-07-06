function encrypt(publicKey, text) {
    let encryptor = new JSEncrypt();
    encryptor.setPublicKey(publicKey);
    console.log(encryptor);
    return encryptor.encrypt(text);
}

$(function(){
    $('#loginBtn').on('click', function(){
        var username = $('#usr').val();
        var password = $('#pwd').val();
        var publicKey = $('#public_key').val();
        var enCryPassword = encrypt(publicKey, password);
        $('#pwd').val(enCryPassword)
    });
})
