/**
 * jquery.snow - jQuery Snow Effect Plugin *
 *
 * @version 21Dec2020
 * @author Ivan Lazarevic // Copyright
 * @author Thomas Lépine // Modification + amélioration pour le besoin du journal
 * @requires jQuery
 *
 * @params minSize - min size of snowflake, 6 by default
 * @params maxSize - max size of snowflake, 20 by default
 * @params newOn - frequency in ms of appearing of new snowflake, 500 by default
 * @params flakeColor - color of snowflake, #FFFFFF by default
 * @example $.fn.snow({ maxSize: 200, newOn: 1000 });
 */

(function ($) {
  $.fn.snow = function (options) {
    var $flocon = $('<div class="flocon" />')
        .css({ position: "absolute", top: "-20px" })
        .html("&#10052;"), // Table des symboles : https://www.toptal.com/designers/htmlarrows/symbols/
    defaults = {
      minSize: 6,
      maxSize: 20,
      newOn: 500,
      flakeColor: "#FFFFFF",
    },
    options = $.extend({}, defaults, options);
    var interval = setInterval(function () {
      var startPositionWidth =
          Math.random() * ($(document).width() - (options.maxSize * 9) / 5),
        startOpacity = 0.33 + (0.4 + Math.random()) / 1.5,
        sizeFlake = options.minSize + Math.random() * options.maxSize,
        endPositionHeight = $(document).height() - 2*options.maxSize,
        endPositionWidth = startPositionWidth,
        durationFall = $(document).height() * 8 + Math.random() * 2500;
      $flocon
        .clone()
        .appendTo("body")
        .css({
          left: startPositionWidth,
          opacity: startOpacity,
          "font-size": sizeFlake,
          color: options.flakeColor,
          "z-index": "1",
        })
        .animate(
          { top: endPositionHeight, left: endPositionWidth, opacity: 0.53 },
          durationFall,
          "linear",
          function () {
            $(this).remove();
          }
        );
    }, options.newOn);
  };
})(jQuery);
