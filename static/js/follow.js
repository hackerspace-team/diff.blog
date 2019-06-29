import { setup_ajax, show_login_prompt_if_required, send_event } from "./helpers";
setup_ajax();

$(function () {
    $("body").on("click", ".following", function() {
        if(show_login_prompt_if_required()) {
            return;
        }
        send_event('unfollow');
        $(this).removeClass("is-light");
        $(this).removeClass("following");
        $(this).addClass("is-dark");
        $(this).addClass("follow");
        $(this).text("Follow");

        $.ajax({
            type: "DELETE",
            url: "/api/user/following",
            data: {"user_id": $(this).data("user-id")},
            success: function(response) {

            }
        })
    });
    $("body").on("click", ".follow", function() {
        if(show_login_prompt_if_required()) {
            return;
        }
        send_event('follow');
        $(this).removeClass("is-dark");
        $(this).removeClass("follow");
        $(this).addClass("is-light");
        $(this).addClass("following");
        $(this).text("Following");

        $.ajax({
            type: "POST",
            url: "/api/user/following",
            data: {"user_id": $(this).data("user-id")},
            success: function(response) {

            }
        })
    });
});