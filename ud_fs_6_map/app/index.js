// CSS requirements
require('./foundation.min.css');
require('./main.css');

import _ from 'lodash';
import ko from 'knockout';
import axios from 'axios';
import {Places} from './model';

(function() {
    'use strict';

    let globalGoogle;
    let map;

    let listing = [];
    let settedMarker  = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png';
    let defaultMarker = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png';

    let fetcher = axios.create({
        baseURL: 'http://52.206.145.58',
        timeout: 2000
    });
    let infowindow;

    function asyncInfoWindow(marker) {
        var title = marker.title;
        fetcher.get('/search/'+title).then(function(response) {
            let data = response.data['businesses'][0];
            let content = `
            <div class='row'>
              <div class='small-7 large-7 columns'>
                <img src='${data['image_url']}' />
              </div>
              <div class='small-5 large-5 columns info-body'>
                <div class='title'>${title}</div>
                <br />

                Phone number: ${data['display_phone'] || 'No phone provided'} <br /><br />
                Price: ${data['price'] || 'No price provided'}<br /> <br />
                Rating: ${data['rating'] || 'No rating provided'} <br /> <br />
                # Reviews: ${data['review_count'] || 'No reviews'} <br /><br />
                <a href='${data['url']}' target=_blank'>Visit on Yelp</a>
             </div>
            </div>`;
            infowindow.setContent(content);
            infowindow.open(map, marker);

        }).catch((error) => {
            infowindow.setContent("<div class='info-body'>ERROR processing request.</div>");
            infowindow.open(map, marker);

        });
    }

    let addInfoMarker = (marker) => {
        marker.addListener('click', function() {
            setSelectedMarker(marker);
            asyncInfoWindow(marker);
        });
    };

    // set visible
    let setMarkerVisible = (markerList) => {
        _.forEach(listing, (item) => {
            item.marker.setVisible(false);
        });
        _.forEach(markerList, (item) => {
            item.marker.setVisible(true);
        });
    };

    let setSelectedMarker = (marker) => {
        _.forEach(listing, (item) => {
            item.marker.setIcon(defaultMarker);
        });
        marker.setIcon(settedMarker);
    };

    // KO Main ViewModel
    function placesViewModel() {
        this.searchData = ko.observable();
        this.places = ko.observableArray(listing);
        // Filter box
        this.filterMarkers = function() {
            let search = this.searchData();
            let newList = listing;
            if (search !== undefined && search !== '') {
                newList = _.filter(this.places(), (item) => {
                    return _.includes(
                        item.title.toLowerCase(),
                        search.toLowerCase()
                    );
                });
            }
            this.places(newList);
            setMarkerVisible(newList);
        };

        // Open Marker
        this.openMarker = function() {
            let item = _.filter(listing, (item) => {
                return item.marker.title == this.title;
            });
            let marker = item[0].marker;
            globalGoogle.maps.event.trigger(marker, 'click');
        };
    };

    // Initialize remote location fetch
    // Register bindings and create markers
    let startLocations = () => {
        fetcher.get('/location').then( (response) => {
            _.forEach(response.data, (item) => {
                let place  = new Places(
                    map, defaultMarker, item.latitude,
                    item.longitude, item.title
                );
                addInfoMarker(place.marker);
                listing.push(place);
            });
            ko.applyBindings(new placesViewModel(),
                             document.getElementById('places'));
        }).catch(function(error) {
            errorScreen();
        });
    };

    // Map initialization callback is required by Google API
    let initMap = () => {
        startLocations();
        globalGoogle = google;
        var latitude = -27.5868015;
        var longitude = -48.505244;
        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: latitude, lng: longitude},
            zoom: 13
        });
        infowindow = new globalGoogle.maps.InfoWindow();
    };

    let errorScreen = () => {
        document.getElementById('map').innerHTML = "ERROR trying to processs your request. Try again later";
    };

    window.initMap = initMap;
    window.errorScreen = errorScreen;

})();
