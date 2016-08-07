jQuery(function($) {
    form = $('.comment-form').clone();
    reply = $('.comment-reply-link');
    cancel = $('.comment-reply-cancel-link');
    cancel.hide();

    reply.click(function(e) {
        e.preventDefault();
        reply.show(); 
        cancel.hide(); 
        comment = $(this).parents('.comment-wrapper');
        comment.find(cancel).show();
        $(this).hide();
        $('.comment-form').remove();        
        num = $(this).attr("data-id");
        urlf = "/comment_reply/" + num;        
        form.clone().attr("action",urlf).appendTo(comment);        
        $('#id_parent').val($(this).data('id'));        
    });

    cancel.click(function(e) {
        e.preventDefault();
        comment = $(this).parents('.comment-wrapper');
        comment.find(reply).show();
        $(this).hide();
        $('.comment-form').remove();
        form.clone().appendTo('.comment-form-container');
    });
});