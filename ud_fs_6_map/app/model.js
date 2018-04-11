import axios from 'axios';

export class Places {
    constructor(map, icon, latitude, longitude, title) {
        this.latitude = latitude;
        this.longitude = longitude;
        this.title = title;
        let latlng = {'lat': this.latitude, 'lng': this.longitude};
        this.marker = new google.maps.Marker({
            position: latlng,
            title: this.title,
            map: map,
            icon: icon
        });
    }
}
