create table if not exists Account
(
    id              integer not null
        constraint Account_pk
            primary key autoincrement,
    name            nvarchar default 'account' not null,
    enc_private_key varchar not null,
    imported        boolean  default false not null
);

create unique index if not exists Account_id_uindex
    on Account (id);

create table if not exists Wallet
(
    enc_seed_phrase varchar not null,
    count           integer default 0 not null,
    password_hash   varchar not null
);
