# Change Log

All notable changes to this project are documented in this file.


## 0.0.9 - 2015-06-30

* Switch to semistandard-format (that performs semicolon insertion) to reformat source code since
  the lack of semicolon broke some builds.


## 0.0.8 - 2015-06-29

* Added pie chart example.
* Added categories chart example.
* Removed development dependency on CoffeeScript. Use plain old ES5.
* Forward "plotclick" and "plothover" events to controller (thanks to Itsiki Avidan) [#21, #22].


## 0.0.6 - 2014-09-18

### Changed

* __BREAKING CHANGE__: Initial watch is done with scope.$watch instead of scope.$watchCollection.
