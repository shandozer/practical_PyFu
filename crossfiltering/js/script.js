        var dataTable = dc.dataTable("#dc-table-graph");

        var magnitudeChart = dc.barChart("#dc-magnitude-chart");

        var depthChart = dc.barChart("#dc-depth-chart");

        var timeChart = dc.lineChart("#dc-time-chart");

        d3.csv("data/quakes.csv", function(data) {

            var dtgFormat = d3.time.format("%Y-%m-%dT%H:%M:%S");

            data.forEach(function(d) {

                d.dtg = dtgFormat.parse(d.origintime.substr(0,19));
                d.lat = +d.latitude;
                d.long = +d.longitude;
                d.mag = d3.round(+d.magnitude,1);
                d.depth = d3.round(+d.depth,0);
            });

            var facts = crossfilter(data);

            var magValue = facts.dimension(function(d) {
                return d.mag;
            });

            var magValueGroupCount = magValue.group()
                .reduceCount(function(d) { return d.mag; });

            var depthValue = facts.dimension(function(d) {
                return d.depth;
            });

            var depthValueGroup = depthValue.group();

            var volumeByHour = facts.dimension(function(d) {
               return d3.time.hour(d.dtg);
            });

            var volumeByHourGroup = volumeByHour.group()
                .reduceCount(function(d) { return d.dtg; });

            var timeDimension = facts.dimension(function(d) {
                return d.dtg;
            });


            magnitudeChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(magValue)
                .group(magValueGroupCount)
                .transitionDuration(500)
                .centerBar(true)
                .gap(65)
                .filter([3,5])
                .x(d3.scale.linear().domain([0.5, 7.5]))
                .elasticY(true)
                .xAxis().tickFormat();


            depthChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(depthValue)
                .group(depthValueGroup)
                .transitionDuration(500)
                .centerBar(true)
                .gap(1)
                .x(d3.scale.linear().domain([0, 100]))
                .elasticY(true)
                .xAxis().tickFormat(function(v) { return v;});

            timeChart.width(960).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(volumeByHour)
                .group(volumeByHourGroup)
                .transitionDuration(500)
                .elasticY(true)
                .x(d3.time.scale().domain([new Date(2013, 6, 18), new Date(2013, 6, 24)]))
                .xAxis();

            //Table of quake data setup
            dataTable.width(960).height(800)
                .dimension(timeDimension)
                    .group(function(d) {
                        return "Earthquake Table"
                    })
                    .size(15)
                .columns([
                    function(d) {return d.dtg; },
                    function(d) {return d.lat; },
                    function(d) {return d.long; },
                    function(d) {return d.depth; },
                    function(d) {return d.mag; },

                    function(d) {
                        return '<a href=\"http://maps.google.com/maps?z=12&t=m&q=loc:' + d.lat + '+' +
                            d.long + "\" target=\"_blank\"> Google Map</a>"},
                    function(d) {
                        return '<a href=\"http://www.openstreetmap.org/?mlat=' + d.lat + '&mlon=' + d.long +
                            '&zoom=12' + "\" target=\"_blank\"> OSM Map</a>"}
                ])
                .sortBy(function(d) {return d.dtg; })
                .order(d3.ascending);

            dc.renderAll();
    });