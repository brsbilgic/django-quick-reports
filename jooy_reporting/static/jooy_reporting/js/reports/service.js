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

        function get(content_type_id, report_slug) {
            return $http.get('api/models/'+content_type_id+'/chart/?report_slug='+report_slug);
        }
    }


})();