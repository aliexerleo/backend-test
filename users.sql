-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    "Id" bigint NOT NULL,
    "FullName" text COLLATE pg_catalog."default",
    "Birth" date,
    "Email" text COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY ("Id")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to myschool;