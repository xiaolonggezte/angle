
var easing = Deck.easing
var prefix = Deck.prefix

var transform = prefix('transform')
var transition = prefix('transition')
var transitionDelay = prefix('transitionDelay')
var boxShadow = prefix('boxShadow')

var translate = Deck.translate

var $container = document.getElementById('container')
var $topbar = document.getElementById('topbar')



var deck = Deck()

deck.mount($container)
