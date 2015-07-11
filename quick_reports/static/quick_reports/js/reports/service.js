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

        function get(appLabel, modelName, reportSlug) {
            return $http.get('api/apps/'+appLabel+'/'+modelName+'/?report_slug='+reportSlug);
        }
    }


})();