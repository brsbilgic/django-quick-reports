(function () {
    'use strict';

    angular
        .module('jrApp.report.controllers')
        .controller('ReportController', ReportController);

    ReportController.inject = ['$stateParams', 'Reports'];
    function ReportController($stateParams, Reports) {
        var vm = this;


        activate();
        function activate() {
            console.log($stateParams);
            Reports.get($stateParams.appLabel, $stateParams.modelName, $stateParams.reportSlug)
                .then(fnSuccess);

            function fnSuccess(data) {
                vm.data = data.data.data;
                vm.app_label = data.data.app_label;
                vm.model_name = data.data.model_name;
                vm.report = data.data.report;
                vm.myData = [data.data.data];


                vm.myChartOptions = {
                    series: {
                        lines: {
                            show: false
                        },
                        points: {
                            show: true,
                            radius: 4
                        },
                        splines: {
                            show: true,
                            tension: 0.2,
                            lineWidth: 2,
                            fill: 0.4
                        }
                    },
                    grid: {
                        hoverable: true,
                        clickable: true
                    },
                    tooltip: true,
                    tooltipOpts: {
                        content: '%x : %y'
                    },
                    xaxis: {
                        mode:"time",
                        minTickSize: [1, "day"],
                        timeformat: "%d/%m/%y"
                    },
                    yaxis: {
                        min: 0,
                        minTickSize: 5,
                        tickDecimals:0
                    }

                };

            }
        }
    }

})();