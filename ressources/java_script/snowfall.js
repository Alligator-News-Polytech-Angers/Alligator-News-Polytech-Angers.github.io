/**
 * jquery.snow - jQuery Snow Effect Plugin *
 *
 * @version 21Jan2012
 * @author Ivan Lazarevic // Copyright
 * Thomas Lépine // Modification
 * @requires jQuery
 *
 * @params minSize - min size of snowflake, 10 by default
 * @params maxSize - max size of snowflake, 20 by default
 * @params newOn - frequency in ms of appearing of new snowflake, 500 by default
 * @params flakeColor - color of snowflake, #FFFFFF by default
 * @example $.fn.snow({ maxSize: 200, newOn: 1000 });
 */

(function ($) {
  $.fn.snow = function (options) {
    var $flocon = $('<div id="flocon" />')
        .css({ position: "absolute", top: "-25px" })
        .html("&#10052;"), // Table des symboles : https://www.toptal.com/designers/htmlarrows/symbols/
      documentHeight = $(document).height(),
      documentWidth = $(document).width(),
      defaults = {
        minSize: 10,
        maxSize: 20,
        newOn: 500,
        flakeColor: "#FFFFFF",
      },
      options = $.extend({}, defaults, options);
    var interval = setInterval(function () {
      var startPositionWidth = Math.random() * (documentWidth - options.maxSize*9/5),
        startOpacity = 0.2 + (0.5 + Math.random()) / 1.5,
        sizeFlake = options.minSize + Math.random() * options.maxSize,
        endPositionHeight = documentHeight,
        endPositionWidth = startPositionWidth,
        durationFall = documentHeight * 8 + Math.random() * 2500;
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
          { top: endPositionHeight, left: endPositionWidth, opacity: 0.53},
          durationFall,
          "linear",
          function () {
            $(this).remove();
          }
        );
    }, options.newOn);
  };
})(jQuery);
