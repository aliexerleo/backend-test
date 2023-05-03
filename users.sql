-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    "Id" integer NOT NULL,
    "FullName" text COLLATE pg_catalog."default",
    "Birth" timestamp without time zone,
    "Email" text COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY ("Id")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;