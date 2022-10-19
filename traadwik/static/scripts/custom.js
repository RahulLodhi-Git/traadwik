// Header Box
$('.search-icon i, .search-wrap .s-form i').click(function(){
    $('body').toggleClass('search-open')
})

// mobile menu triger
$('.mobile-toggle i').click(function(){
    $('body').toggleClass('mobile-open')
})
$('.desktop-menu ul>li i').click(function(){
    $(this).parent('li').siblings('li').removeClass('child-open')
    $(this).parent('li').siblings('li').children('ul').slideUp(300)
    $(this).parent('li').toggleClass('child-open')
    $(this).parent('li').children('ul').slideToggle(300)
})