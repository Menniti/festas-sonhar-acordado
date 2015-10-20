var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');

gulp.task('vendor-js', function() {
    return gulp.src([
            'bower_components/jquery/dist/jquery.js',
            'bower_components/angular/angular.js',
            'bower_components/angular-resource/angular-resource.js',
            'bower_components/bootstrap/dist/js/bootstrap.js'
        ])
       .pipe(concat('library.js'))
       .pipe(uglify())
       .pipe(gulp.dest('grandesfestas/assets/vendor'));
});

gulp.task('vendor-css', function() {
    return gulp.src([
            'bower_components/bootstrap/dist/css/bootstrap.min.css',
        ])
       .pipe(concat('library.css'))
       .pipe(gulp.dest('grandesfestas/assets/vendor'));
});

gulp.task('vendor', ['vendor-js', 'vendor-css']);
gulp.task('default', ['vendor']);