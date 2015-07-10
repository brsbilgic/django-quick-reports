(function() {
    'use strict';

    angular
        .module('jrApp.report.services')
        .factory('Reports', Reports);

    Reports.inject = ['$http'];

    function Reports($http) {
        return {
            'get': get
        };

        function get(modelName, reportSlug) {
            return $http.get('api/models/'+modelName+'/?report_slug='+reportSlug);
        }
    }


})();