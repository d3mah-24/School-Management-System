alert(123);
console.log("dwsdvfdgf");
$(document).ready(function () {
    $(document).on('click', '#submit', function (e) {

        let formData = new FormData();
        let all = {"test": 123};
        var temp = {};
        var body1 = document.querySelector("div.er");

        const $$ = document.querySelectorAll.bind(document);
        var alltr = $$('tr');
        var allinp = document.querySelectorAll("tr > td > input");
        alert(allinp.length);

        var id = document.querySelectorAll(".er > .id").value;

        for (let index = 0; index < alltr.length; index++) {

            temp = {
                'id': id, 'ten1': allinp[0].value, 'ten2': allinp[1].value,
                'ten3': allinp[2].value,
                'twenty': allinp[3].value,
                'fifty': allinp[4].value,
                'hundred': allinp[5].value,

            }
            all[id] = temp;
            temp = {};
        }


        $.ajax({
            type: 'POST',
            url: '{% url "mark" %}',
            data: all,
            cache: false,
            processData: false,
            contentType: false,
            enctype: 'multipart/form-data',
            success: function () {
                alert('The post has been created!')
            },
            error: function (xhr, errmsg, err) {
                alert(xhr.status + ":" + xhr.responseText)
            }
        })
    });
});

