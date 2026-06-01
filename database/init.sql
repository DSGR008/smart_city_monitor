create table traffic_data (
    id serial primary key,
    vehicle_id varchar(20) not null,
    vehicle_count int not null,
    avg_speed float not null,
    trafficlevel varchar(20) not null,
    timstamp timestamp not null
);
