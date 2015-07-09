(function () {
    'use strict';

    angular
        .module('jrApp.report.controllers')
        .controller('ReportController', ReportController);

    ReportController.inject = ['$stateParams', 'Reports'];

    console.log("1");

    function ReportController($stateParams, Reports) {
        var vm = this;


        activate();
        function activate() {
            console.log($stateParams);
            Reports.get($stateParams.contentTypeId, $stateParams.reportSlug)
                .then(fnSuccess);

            function fnSuccess(data) {
                vm.data = data.data.data;
                vm.ct = data.data.ct;
                vm.myData = [data.data.data];


                vm.myChartOptions = {
                    series: {
                        lines: {
                            show: true
                        },
                        points: {
                            show: true
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