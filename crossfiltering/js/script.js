        var dataTable = dc.dataTable("#dc-table-graph");

        var ageChart = dc.barChart("#dc-magnitude-chart");

        var IQChart = dc.barChart("#dc-depth-chart");

        var dayOfWeekChart = dc.rowChart("#dc-dayweek-chart");

        var genderChart = dc.pieChart("#dc-island-chart");

        var dxChart = dc.pieChart("#dc-dx-chart");

        var subtypeChart = dc.pieChart("#dc-subtype-chart");

        var timeChart = dc.lineChart("#dc-time-chart");

        var motionTimeChart = dc.lineChart("#dc-motiontime-chart");

        var motionFrameChart = dc.barChart("#dc-motionframes-chart");

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
                d.motionTime = +d.motion_Time;
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

            var motionByMinutes = facts.dimension(function(d) {
               return d.motionTime;
            });

            var motionByMinutesGroup = motionByMinutes.group()
                .reduceCount(function(d) { return d.motionTime; });

            var motionFramesValue = facts.dimension(function(d) {
               return d.motionFrames;
            });

            var motionFramesValueGroup = motionFramesValue.group();

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
                    return "Other Groups";
                });

            var diagnosisGroup = diagnosis.group();

            var subType = facts.dimension(function (d) {
                if (d.SubType == 1 )
                    return "Group1";
                else if (d.SubType == 2)
                    return "Group2";
                else if (d.SubType == 3)
                    return "Group3";
                else if (d.SubType == 4)
                    return "Group4";
                else if (d.SubType == 5)
                    return "Group5";
                else
                    return "Other Groups";
                });

            var subTypeGroup = subType.group();

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
                .filter([8,12])
                .x(d3.scale.linear().domain([6, 18]))
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

            //motion frames bar chart
            motionFrameChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(motionFramesValue)
                .group(motionFramesValueGroup)
                .transitionDuration(500)
                .centerBar(true)
                .gap(55)
                .elasticY(true)
                .x(d3.scale.linear().domain([0, 360]))
                .xAxis().tickFormat();

            //motion time bar chart
//            ageChart.width(480).height(150)
//                .margins({top: 10, right: 10, bottom: 20, left: 40})
//                .dimension(ageValue)
//                .group(ageValueGroupCount)
//                .transitionDuration(500)
//                .centerBar(true)
//                .gap(65)
//                .filter([6,25])
//                .x(d3.scale.linear().domain([6, 18]))
//                .elasticY(true)
//                .xAxis().tickFormat();

            //scans per day line chart
            timeChart.width(960).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(volumeByHour)
                .group(volumeByHourGroup)
                .transitionDuration(500)
                .elasticY(true)
                .x(d3.time.scale().domain([new Date(2010, 1, 1), new Date(2016, 4, 30)]))
                .xAxis().tickFormat();

            //motion_Time line chart
            motionTimeChart.width(480).height(150)
                .margins({top: 10, right: 10, bottom: 20, left: 40})
                .dimension(motionByMinutes)
                .group(motionByMinutesGroup)
                .transitionDuration(500)
                .elasticY(true)
                .x(d3.time.scale().domain([0, 1000.0]))
                .xAxis().tickFormat();

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

            subtypeChart.width(250).height(220)
                .radius(100)
                .innerRadius(30)
                .dimension(subType)
                .group(subTypeGroup)
                .title(function(d) { return d.value;});

            //Table of quake data setup
            dataTable.width(960).height(800)
                .dimension(timeDimension)
                    .group(function(d) {
                        return "Scans"
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
                    function(d) {return d.motionFrames; },
                    function(d) {return d.motionTime; }
                ])
                .sortBy(function(d) {return d.dtg; })
                .order(d3.ascending);

            dc.renderAll();
    });