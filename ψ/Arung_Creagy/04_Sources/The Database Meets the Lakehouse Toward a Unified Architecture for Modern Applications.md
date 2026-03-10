---
type: web clipped
status:
  - current
tags:
  - data_system
capture_date: 2025-11-18
url: https://www.tigerdata.com/blog/the-database-meets-the-lakehouse-toward-a-unified-architecture-for-modern-applications#the-limits-of-the-oltp-vs-olap-dichotomy
relevance to: "[[Implementing a Data Lakehouse A Best Practices Guide]]"
---
>[!key] Insight
>- OLTP/OLAP dichotomy does not fit today's business requirement. optimization for reading and writing only does not answer to important use cases.
>- The database technology at database level can still be useful for operational database
>- A more useful categorization; operational databases that power products, and lakehouses that power organizations
>- The operational databases are overseen by product engineering teams, while the lakehouses are maintained by data teams
>- Operational  Medallion Architecture
>	- **Bronze Layer:** Raw data lives in Parquet or Iceberg files on AWS S3 or similar low-cost bottomless storage systems. This data is typically immutable, append-only, and queryable by anything: query engines like AWS Athena, DuckDB, Trino, ClickHouse, or Polars, or even directly from an operational database like Postgres.
>	- **Operational Silver Layer:** Cleaned, filtered, validated, and deduplicated data is written into Postgres to power real-time analytics, dashboards, or application logic of user-facing products.
>	- **Operational Gold Layer:** Pre-aggregated data over silver data (like Postgres’ materialized views or TimescaleDB’s continuous aggregates) serve low-latency, high-concurrency product experiences. **These are typically maintained within the database to ensure consistency between silver and gold layers**.
>- You can roll up aggregates from Iceberg (bronze) into Postgres tables (silver) or vice versa

**TL;DR:** The OLTP/OLAP split no longer fits how developers build today. Postgres and the lakehouse are now used side-by-side – but stitched together with brittle pipelines. We think they belong in a single, modular system: open formats, bidirectional sync, and real-time performance by default.

The architecture of modern data systems is undergoing a fundamental shift.

Ask a developer how they build data systems today, and the answer increasingly looks like this: Postgres for the application, a lakehouse for the analytics and data science.

Postgres, long favored for transactional workloads, has evolved into a general-purpose operational database. It’s trusted, flexible, and deeply extensible, powering everything from customer transactions and CRUD apps, to real-time dashboards and AI-backed product features. Its ecosystem has grown to support real-time analytics ([TimescaleDB](https://github.com/timescale/timescaledb)), geospatial data (PostGIS), vector and full-text search (pgvector and pgvectorscale), and more.

At the same time, the rise of open lakehouse technologies has redefined how organizations manage and analyze data at scale. Disaggregated storage, open table formats like Iceberg, structured data catalogs, and composable query engines have made it possible to analyze petabyte-scale data with precision and control. This architecture can offer governance, avoid vendor lock-in, and still provide data teams flexibility in their choice of tools.

What’s striking isn’t just the success of these technologies individually, but how often they’re now being deployed together. Organizations increasingly need to support both operational workloads (powered by databases) and non-operational workloads (powered by lakehouses), often using data from the same sources – people, machines, digital systems, or agents. Yet these systems are still treated in isolation, often owned by different teams, with too much friction in making them work together seamlessly.

We believe that friction should not exist. In fact, we think a new, more coherent architecture is emerging: one that treats Postgres and the lakehouse not as separate worlds, but as distinct layers of a single, modular system, designed to meet the full spectrum of operational and analytical needs.

## The Limits of the OLTP vs OLAP Dichotomy

The old way of thinking about databases was simple: OLTP for transactions, OLAP for analysis. You used Postgres to power your app, and sent nightly ETL jobs to a data warehouse for internal reports and dashboards. This traditional distinction served us well when applications were simpler, and internal reporting could live on a much slower cadence. But that’s no longer the case.

Modern applications are data-heavy, customer-facing, and real-time by design. **They blur the lines between transactional and analytical**.

>[!warning] However, if the application is more static, does it mean we still cann use the classic architecture?
>the answer is below

- A financial app might run a trading engine that needs millisecond access to customer portfolios, while simultaneously feeding real-time risk reports and internal dashboards.
- A SaaS app isn’t just storing clicks – it’s calculating usage metrics, triggering alerts, and serving personalized models.
- An industrial monitoring system might ingest tens of millions of sensor readings per hour, drive anomaly detection and alerting logic, and archive years of telemetry for long-term analytics and AI model training.

These use cases are not outliers – they are quickly becoming the norm.

**We increasingly see a more useful split: operational databases that power products, and lakehouses that power organizations.**

Yet even though ownership of these types of systems are split – product-engineering teams responsible for the operational systems powering their products, and data teams responsible for managing lakehouse systems as organizational services – the two still need to talk to each other. They need to work on the same data and often share underlying schemas. The better they integrate and remain in sync, the more resilient and capable the system becomes.

## An Operational Medallion Architecture

One pattern we see gaining traction is what we call an ***operational medallion architecture***. Inspired by the medallion models popularized in the data engineering world, this pattern also incorporates bronze, silver, and gold layers – not just for internal analytics, but for powering real-time, user-facing systems as well.

Here’s what that looks like:

- **Bronze Layer:** Raw data lives in Parquet or Iceberg files on AWS S3 or similar low-cost bottomless storage systems. This data is typically immutable, append-only, and queryable by anything: query engines like AWS Athena, DuckDB, Trino, ClickHouse, or Polars, or even directly from an operational database like Postgres.
- **Operational Silver Layer:** Cleaned, filtered, validated, and deduplicated data is written into Postgres to power real-time analytics, dashboards, or application logic of user-facing products.
- **Operational Gold Layer:** Pre-aggregated data over silver data (like Postgres’ materialized views or TimescaleDB’s continuous aggregates) serve low-latency, high-concurrency product experiences. These are typically maintained within the database to ensure consistency between silver and gold layers.

Crucially, each layer is queryable, and this movement of data is bidirectional. You can pull raw or transformed data from S3 directly into Postgres (akin to tightly integrated reverse ETL). You can roll up aggregates from Iceberg into Postgres tables (by one-off or standing queries against Iceberg files from Postgres). ` You can continuously sync a full schema or a single table from the database to the lakehouse.`

Much as bronze (or transformed) data can be read from the lakehouse storage layer on S3 into the database, silver and gold in the database can be written to these lakehouse storage formats. This avoids needing to re-implement identical pipelines in both systems, which both adds complexity and risks consistency.

One common pattern we’ve observed in applications requiring fresh data is writing from an upstream streaming system like Kafka or Kinesis *in parallel* to both S3 (for row, unmodified bronze data) and Postgres (relying on database schemas and constraints for data validation). Then these silver tables and subsequent gold aggregates in the database are exported out to S3 again, so data teams now have access to the “ground truth data” that had been served to customers.

Now, each system maintains its separation of concerns. The operational database can run locked down – both to users and unfriendly queries – while data is still made available as part of the open lakehouse wherever it’s needed in the org.

## Why Now? Technical Forces Driving the Shift

Several developments are powering this shift from the operational databases and lakehouses from being siloed to integrated.

First, Iceberg has matured into a stable and flexible table format that supports schema evolution, ACID transactions, and efficient compaction. It enables multiple compute engines to read from and write to the same datasets – with catalog layers that track metadata and enforce governance across the stack. Much like databases had catalogs at their core, so now do lakehouses.

Second, Postgres has continued to evolve as a platform. With extensions for columnar storage, time-series data, and vector and hybrid search – what we’ve been building at Timescale for years – Postgres now serves many products that incorporate real-time analytics and agentic workflows directly. And with emerging support for querying S3 and Iceberg data directly from within Postgres, it is increasingly possible to incorporate S3-hosted data directly. So Postgres is no longer for just transactional data – with one-way ETL/CDC to lakehouse – but **now acts as the serving layer for products incorporating both transactional and analytical data.** This isn’t just a data caching layer for pre-computed data, but a full-fledged SQL database for further aggregations, enrichment, or JOINs at query time.

Third, developers expect composability. Some organizations may be stuck with their legacy monolithic data platforms, but most developers and data scientists want flexibility to compose their own stacks, integrating familiar tools in ways that reflect their application’s needs. The shift toward open formats and disaggregated storage fits this mindset. So does the desire for control, particularly in regulated industries or where data sovereignty matters.

**Put differently: the market is moving toward modular, open, developer-friendly architectures.**

We believe the future of data infrastructure will be shaped by systems that integrate operational and analytical layers more deeply—systems that treat Postgres and the lakehouse as two sides of the same coin.

This won’t happen through another proprietary monolith. It will come from careful interfaces – incremental sync, shared catalogs, unified query surfaces – and from an architectural philosophy that embraces heterogeneity rather than fighting it.

**We call this architecture the “BaseLake.”**

Much as the “Lakehouse” was a portmanteau of a “data lake” and “data warehouse,” representing one architecture that combines features of both, we think this new emerging architecture similarly combines capabilities of databases and lakehouses.

Over the past year, we’ve been building such a BaseLake. An open, composable architecture that rests on the strengths of Postgres and Iceberg, tightly integrates with existing lakehouse systems, and makes it dramatically easier to build full-stack data systems with operational and analytical fidelity.

This isn’t about using ETL to move data from legacy systems to new systems – it’s about a coherent modern data architecture that serves operational and non-operational use cases, alike.

Stay tune