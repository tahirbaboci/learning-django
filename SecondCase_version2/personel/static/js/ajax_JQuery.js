


 $(document).ready(function(){
         $('#submit').click(function(event){
            $('#message').html("<h2>button has been clicked</h2>");
            event.preventDefault();
            var nome = $("#nome").data();
            var email = $("#email").data();
            var data = {
               "nome" : nome,
               "email" : email,
            };
            $.ajax({
              type: "POST",
              url: "/add_me/",
              data: data,
              success: function(){ $('#message').html("<h2>Contact Form Submitted!</h2>")},
              dataType: "json",
              contentType : "application/json"

            });
            return false;
         });

        $("#email").change(function () {
          var validateEmail = $(this).val();

          $.ajax({
            url: '/ajax/validate_email/',
            data: {
              'email': validateEmail,
            },
            dataType: 'json',
            success: function (data) {
              if (data.is_taken) {
                alert("A user with this username already exists.");
              }
            }
          });

        });
 });
