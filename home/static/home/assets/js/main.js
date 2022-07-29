jQuery(document).ready(function($) {

    //// hide #back-top first
    $(".scrollToTop").hide();

    // fade in #back-top
    $(function() {
        $(window).scroll(function() {
            if ($(this).scrollTop() > 100) {
                $('.scrollToTop').fadeIn();
            } else {
                $('.scrollToTop').fadeOut();
            }
        });

        // scroll body to 0px on click
        $('.scrollToTop').click(function() {
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });
    });

    $(function() {
        $('a.page-scroll').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 0
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
    });


    // collasped menu on click
    $(".navbar-nav li a").click(function(event) {
        if (!$(this).parent().hasClass('dropdown'))
            $(".navbar-collapse").collapse('hide');
    });

});


(function($) {
    "use strict"

    // Mobile dropdown
    $('.has-dropdown>a').on('click', function() {
        $(this).parent().toggleClass('active');
    });

    // Aside Nav
    $(document).click(function(event) {
        if (!$(event.target).closest($('#nav-aside')).length) {
            if ($('#nav-aside').hasClass('active')) {
                $('#nav-aside').removeClass('active');
                $('#nav').removeClass('shadow-active');
            } else {
                if ($(event.target).closest('.aside-btn').length) {
                    $('#nav-aside').addClass('active');
                    $('#nav').addClass('shadow-active');
                }
            }
        }
    });

    $('.nav-aside-close').on('click', function() {
        $('#nav-aside').removeClass('active');
        $('#nav').removeClass('shadow-active');
    });

})(jQuery);

'use strict';
var _createClass = function() {
    function defineProperties(target, props) {
        for (var i = 0; i < props.length; i++) {
            var descriptor = props[i];
            descriptor.enumerable = descriptor.enumerable || false;
            descriptor.configurable = true;
            if ("value " in descriptor) descriptor.writable = true;
            Object.defineProperty(target, descriptor.key, descriptor);
        }
    }
    return function(Constructor, protoProps, staticProps) {
        if (protoProps) defineProperties(Constructor.prototype, protoProps);
        if (staticProps) defineProperties(Constructor, staticProps);
        return Constructor;
    };
}();

function _classCallCheck(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function ");
    }
}

var StickyNavigation = function() {
    function StickyNavigation() {
        var _this = this;

        _classCallCheck(this, StickyNavigation);

        this.currentId = null;
        this.currentTab = null;
        this.tabContainerHeight = 70;
        var self = this;
        $('.stickyhero-tab').click(function(event) {
            self.onTabClick(event, $(this));
        });
        $(window).scroll(function() {
            _this.onScroll();
        });
        $(window).resize(function() {
            _this.onResize();
        });
    }

    _createClass(StickyNavigation, [{
        key: 'onTabClick',
        value: function onTabClick(event, element) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: $(element.attr('href')).offset().top - 54
            }, 1500, 'easeInOutExpo');
        }
    }, {
        key: 'onScroll',
        value: function onScroll() {
            this.checkTabContainerPosition();
            this.findCurrentTabSelector();
        }
    }, {
        key: 'onResize',
        value: function onResize() {
            if (this.currentId) {
                this.setSliderCss();
            }
        }
    }, {
        key: 'checkTabContainerPosition',
        value: function checkTabContainerPosition() {
            var offset = $('.stickyhero-tabs').offset().top + $('.stickyhero-tabs').height() - this.tabContainerHeight;
            if ($(window).scrollTop() > offset) {
                $('.stickyhero-tabs-container').addClass('stickyhero-tabs-container--top');
            } else {
                $('.stickyhero-tabs-container').removeClass('stickyhero-tabs-container--top');
            }
        }
    }, {
        key: 'findCurrentTabSelector',
        value: function findCurrentTabSelector(element) {
            var newCurrentId = void 0;
            var newCurrentTab = void 0;
            var self = this;
            $('.stickyhero-tab').each(function() {
                var id = $(this).attr('href');
                var offsetTop = $(id).offset().top - self.tabContainerHeight;
                var offsetBottom = $(id).offset().top + $(id).height() - self.tabContainerHeight;
                if ($(window).scrollTop() > offsetTop && $(window).scrollTop() < offsetBottom) {
                    newCurrentId = id;
                    newCurrentTab = $(this);
                }
            });
            if (this.currentId != newCurrentId || this.currentId === null) {
                this.currentId = newCurrentId;
                this.currentTab = newCurrentTab;
                this.setSliderCss();
            }
        }
    }, {
        key: 'setSliderCss',
        value: function setSliderCss() {
            var width = 0;
            var left = 0;
            if (this.currentTab) {
                width = this.currentTab.css('width');
                left = this.currentTab.offset().left;
            }
            $('.stickyhero-tab-slider').css('width', width);
            $('.stickyhero-tab-slider').css('left', left);
        }
    }]);

    return StickyNavigation;
}();
new StickyNavigation();