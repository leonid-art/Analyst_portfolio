-- ============================================================
--  Стартап-экосистема: создания таблиц
--  Порядок создания учитывает зависимости между таблицами
-- ============================================================

-- 1. company
CREATE TABLE company (
    id                 SERIAL        PRIMARY KEY,
    name               VARCHAR(255)  NOT NULL,
    category_code      VARCHAR(100),
    status             VARCHAR(50)   CHECK (status IN ('acquired', 'operating', 'ipo', 'closed')),
    founded_at         DATE,
    closed_at          DATE,
    domain             VARCHAR(255),
    twitter_username   VARCHAR(100),
    country_code       VARCHAR(3),
    investment_rounds  INTEGER       DEFAULT 0,
    funding_rounds     INTEGER       DEFAULT 0,
    funding_total      NUMERIC(20, 2),
    milestones         INTEGER       DEFAULT 0,
    created_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- 2. people
CREATE TABLE people (
    id                 SERIAL        PRIMARY KEY,
    first_name         VARCHAR(100),
    last_name          VARCHAR(100),
    company_id         INTEGER       REFERENCES company(id),
    twitter_username   VARCHAR(100),
    created_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- 3. education
CREATE TABLE education (
    id                 SERIAL        PRIMARY KEY,
    person_id          INTEGER       NOT NULL REFERENCES people(id),
    degree_type        VARCHAR(50),
    instituition       VARCHAR(255),
    graduated_at       DATE,
    created_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- 4. fund
CREATE TABLE fund (
    id                  SERIAL        PRIMARY KEY,
    name                VARCHAR(255)  NOT NULL,
    founded_at          DATE,
    domain              VARCHAR(255),
    twitter_username    VARCHAR(100),
    country_code        VARCHAR(3),
    investment_rounds   INTEGER       DEFAULT 0,
    invested_companies  INTEGER       DEFAULT 0,
    milestones          INTEGER       DEFAULT 0,
    created_at          TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- 5. funding_round
CREATE TABLE funding_round (
    id                   SERIAL        PRIMARY KEY,
    company_id           INTEGER       NOT NULL REFERENCES company(id),
    funded_at            DATE,
    funding_round_type   VARCHAR(50),
    raised_amount        NUMERIC(20, 2),
    pre_money_valuation  NUMERIC(20, 2),
    participants         INTEGER       DEFAULT 0,
    is_first_round       INTEGER       DEFAULT 0,
    is_last_round        INTEGER       DEFAULT 0,
    created_at           TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at           TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- 6. investment
CREATE TABLE investment (
    id                SERIAL     PRIMARY KEY,
    funding_round_id  INTEGER    NOT NULL REFERENCES funding_round(id),
    company_id        INTEGER    REFERENCES company(id),
    fund_id           INTEGER    REFERENCES fund(id),
    created_at        TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP  DEFAULT CURRENT_TIMESTAMP
);

-- 7. acquisition
CREATE TABLE acquisition (
    id                    SERIAL        PRIMARY KEY,
    acquiring_company_id  INTEGER       NOT NULL REFERENCES company(id),
    acquired_company_id   INTEGER       NOT NULL REFERENCES company(id),
    term_code             VARCHAR(20)   CHECK (term_code IN ('cash', 'stock', 'cash_and_stock')),
    price_amount          NUMERIC(20, 2),
    acquired_at           DATE,
    created_at            TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    updated_at            TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);