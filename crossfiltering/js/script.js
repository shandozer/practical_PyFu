        var dataTable = dc.dataTable("#dc-table-graph");

        var ageChart = dc.barChart("#dc-magnitude-chart");

        var IQChart = dc.barChart("#dc-depth-chart");

        var dayOfWeekChart = dc.rowChart("#dc-dayweek-chart");

        var genderChart = dc.pieChart("#dc-island-chart");

        var dxChart = dc.pieChart("#dc-dx-chart");

        var timeChart = dc.lineChart("#dc-time-chart");

        d3.csv("data/ADHD_data.csv", function(data) {

            var dtgFormat = d3.time.format("%Y%m%d");

            data.forEach(function(d) {

                d.dtg = dtgFormat.parse(d.Date);
                d.ID = +d.ADHDID;
                d.age = d3.round(+d.Age,1);
                d.sex = d.Sex;
                d.IQ = +d.IQ;
                d.Dx = +d.ADHD_Diagnosis;
                d.SubType = +d.ADHD_Subtype;
                d.motionFrames = +d.motion_Frames;
            });

            var facts = crossfilter(data);

            var all = facts.groupAll();

            var ageValue = facts.dimension(function(d) {
                return d.age;
            });

            var ageValueGroupCount = ageValue.group()
                .reduceCount(function(d) { return d.age; });

            var IQValue = facts.dimension(function(d) {
                return d.IQ;
            });

            var IQValueGroup = IQValue.group();

            var volumeByHour = facts.dimension(function(d) {
               return d3.time.day(d.dtg);
            });

            var volumeByHourGroup = volumeByHour.group()
                .reduceCount(function(d) { return d.dtg; });

            var dayOfWeek = facts.dimension(function(d) {
                var day = d.dtg.getDay();
                switch (day) {
                    case 0:
                        return "0.Sun";
                    case 1:
                        return "1.Mon";
                    case 2:
                        return "2.Tue";
                    case 3:
                        return "3.Wed";
                    case 4:
                        return "4.Thu";
                    case 5:
                        return "5.Fri";
                    case 6:
                        return "6.Sat";
                }

            });

            var dayOfWeekGroup = dayOfWeek.group();

            var genders = facts.dimension(function (d) {
                if (d.sex <2 )
                    return "Male";
                else
                    return "Female";
                });

            var gendersGroup = genders.group();

            var diagnosis = facts.dimension(function (d) {
                if (d.Dx == 1 )
                    return "Group1";
                else if (d.Dx == 2)
                    return "Group2";
                else if (d.Dx == 3)
                    return "Group3";
                else
                    return "Other Group";
                });

            var diagnosisGroup = diagnosis.group();

            var timeDimension = facts.dimension(function(d) {
                return d.dtg;
            });

            //overall data count
            dc.dataCount(".dc-data-count")
                .dimension(facts)
                .group(all);

            //bar chart
            ageChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(ageValue)
                .group(ageValueGroupCount)
                .transitionDuration(500)
                .centerBar(true)
                .gap(65)
                .filter([3,5])
                .x(d3.scale.linear().domain([6, 25]))
                .elasticY(true)
                .xAxis().tickFormat();

            //bar chart
            IQChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(IQValue)
                .group(IQValueGroup)
                .transitionDuration(500)
                .centerBar(true)
                .gap(1)
                .x(d3.scale.linear().domain([70, 160]))
                .elasticY(true)
                .xAxis().tickFormat(function(v) { return v;});

            //line chart
            timeChart.width(960).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(volumeByHour)
                .group(volumeByHourGroup)
                .transitionDuration(500)
                .elasticY(true)
                .x(d3.time.scale().domain([new Date(2013, 1, 1), new Date(2016, 4, 30)]))
                .xAxis();

            //row chart day of week
            dayOfWeekChart.width(300).height(220)
                .margins({top: 5, left: 10, right: 10, bottom: 20})
                .dimension(dayOfWeek)
                .group(dayOfWeekGroup)
                .colors(d3.scale.category10())
                .label(function (d) {
                    return d.key.split(".")[1];
                })
                .title(function(d) { return d.value;})
                .elasticX(true)
                .xAxis().ticks(4);

            // Pie Chart
            genderChart.width(250).height(220)
                .radius(100)
                .innerRadius(30)
                .dimension(genders)
                .group(gendersGroup)
                .title(function(d) { return d.value;});

            dxChart.width(250).height(220)
                .radius(100)
                .innerRadius(30)
                .dimension(diagnosis)
                .group(diagnosisGroup)
                .title(function(d) { return d.value;});

            //Table of quake data setup
            dataTable.width(960).height(800)
                .dimension(timeDimension)
                    .group(function(d) {
                        return "Subjects Table"
                    })
                    .size(50)
                .columns([
                    function(d) {return d.dtg; },
                    function(d) {return d.ID; },
                    function(d) {return d.sex; },
                    function(d) {return d.IQ; },
                    function(d) {return d.age; },
                    function(d) {return d.Dx; },
                    function(d) {return d.SubType; },
                    function(d) {return d.motionFrames; }
                ])
                .sortBy(function(d) {return d.dtg; })
                .order(d3.ascending);

            dc.renderAll();
    });