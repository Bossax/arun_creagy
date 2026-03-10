---
type: web clipped
status: raw
tags: data_system
capture_date: 2025-11-18
url: https://docs.databricks.com/aws/en/lakehouse-architecture/interoperability-and-usability/best-practices
relevance to: "[["
---
This article covers best practices for **interoperability and usability**, organized by architectural principles listed in the following sections.

## 1\. Define standards for integration

### Use standard and reusable integration patterns for external integration

Integration standards are important because they provide guidelines for how data should be represented, exchanged, and processed across different systems and applications. These standards help ensure that data is compatible, high quality, and interoperable across various sources and destinations.

The Databricks Lakehouse comes with a comprehensive [REST API](https://docs.databricks.com/api/workspace/introduction) that allows you to programmatically manage nearly all aspects of the platform. The REST API server runs in the control plane and provides a unified endpoint for managing the Databricks platform.

The REST API provides the lowest level of integration that can always be used. However, the preferred way to integrate with Databricks is to use higher level abstractions such as the [Databricks SDKs](https://docs.databricks.com/aws/en/dev-tools/sdks) or [CLI tools](https://docs.databricks.com/aws/en/dev-tools/cli/). CLI tools are shell-based and allow easy integration of the Databricks platform into CI/CD and MLOps workflows.

### Use optimized connectors to ingest data sources into the lakehouse

Databricks offers a variety of ways to help you ingest data into Delta Lake.

- Databricks provides [optimized connectors for stream messaging services](https://docs.databricks.com/aws/en/ingestion/) such as Apache Kafka for near-real time data ingestion of data.
- Databricks provides built-in integrations to [many cloud-native data systems](https://docs.databricks.com/aws/en/query-federation/) and extensible JDBC support to connect to other data systems.
- One option for integrating data sources without ETL is [Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/). Lakehouse Federation is the query federation platform for Databricks. The term query federation describes a collection of features that allow users and systems to run queries against multiple data sources without having to migrate all the data into a unified system. Databricks uses Unity Catalog to manage query federation. Unity Catalog's data governance and data lineage tools ensure that data access is managed and audited for all federated queries run by users in your Databricks workspaces.

### Use certified partner tools

Organizations have different needs, and no single tool can meet them all. [Partner Connect](https://docs.databricks.com/aws/en/partner-connect/) allows you to explore and easily integrate with our partners, who cover all aspects of the lakehouse: data ingestion, preparation and transformation, BI and visualization, machine learning, data quality, and more. Partner Connect allows you to create trial accounts with selected Databricks technology partners and connect your Databricks workspace to partner solutions from the Databricks UI. Try partner solutions using your data in the Databricks lakehouse, and then adopt the solutions that best meet your business needs.

### Reduce complexity of data engineering pipelines

Investing in reducing the complexity of data engineering pipelines enables scalability, agility and flexibility to be able to expand and innovate faster. Simplified pipelines make it easier to manage and adapt all of the operational needs of a data engineering pipeline: task orchestration, cluster management, monitoring, data quality, and error handling.

Lakeflow Spark Declarative Pipelines is a framework for building reliable, maintainable, and testable data processing pipelines. You define the transformations you want to perform on your data, and Lakeflow Spark Declarative Pipelines handles task orchestration, cluster management, monitoring, data quality, and error handling. See [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/).

[Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/) incrementally and efficiently processes new data files as they arrive in cloud storage. It can reliably read data files from cloud storage. An important aspect of both Lakeflow Spark Declarative Pipelines and Auto Loader is their declarative nature: Without them, one must build complex pipelines that integrate different cloud services - such as a notification service and a queuing service - to reliably read cloud files based on events and to reliably combine batch and streaming sources.

Auto Loader and Lakeflow Spark Declarative Pipelines reduce system dependencies and complexity and greatly improve the interoperability with the cloud storage and between different paradigms such as batch and streaming. As a side effect, the simplicity of the pipelines increases the usability of the platform.

### Use infrastructure as code (IaC) for deployments and maintenance

HashiCorp Terraform is a popular open source tool for creating safe and predictable cloud infrastructure across several cloud providers. See [Operational Excellence: Use Infrastructure as code for deployments and maintenance](https://docs.databricks.com/aws/en/lakehouse-architecture/operational-excellence/best-practices#iac)

## 2\. Utilize open interfaces and open data formats

### Use open data formats

Using an open data format means there are no restrictions on its use. This is important because it removes barriers to accessing and using the data for analysis and driving business insights. Open formats, such as those built on Apache Spark, also add features that boost performance with support for ACID transactions, unified streaming, and batch data processing. Furthermore, open source is community-driven, meaning the community is constantly working on improving existing features and adding new ones, making it easier for users to get the most out of their projects.

The primary data format used in the Data Intelligence Platform is Delta Lake, a [fully open data format](https://delta.io/) that offers many benefits, from reliability features to performance enhancements, see [Use a data format that supports ACID transactions](https://docs.databricks.com/aws/en/lakehouse-architecture/reliability/best-practices#delta-lake) and [Best practices for performance efficiency](https://docs.databricks.com/aws/en/lakehouse-architecture/performance-efficiency/best-practices).

Because it's open source, Delta Lake has a large ecosystem. Dozens of third-party tools and applications [support Delta Lake](https://delta.io/integrations). To further enhance interoperability, [Delta tables can be read with Apache Iceberg reader clients](https://docs.databricks.com/aws/en/delta/uniform). A single copy of the data files serves both formats, ensuring the right metadata for the different readers.

### Enable secure data and AI sharing for all data assets

Sharing data and AI assets can lead to better collaboration and decision making. However, when sharing data, it's important to maintain control, protect your data, and ensure compliance with relevant data sharing laws and regulations.

[Delta Sharing](https://docs.databricks.com/aws/en/delta-sharing/) is an open protocol developed by Databricks for securely sharing data with other organizations, regardless of the computing platforms they use. If you want to share data with users outside of your Databricks workspace, regardless of whether they use Databricks, you can use open Delta Sharing to securely share your data. If you want to share data with users who have a Databricks workspace that is enabled for Unity Catalog, you can use Databricks-to-Databricks Delta Sharing.

In both cases, you can share [tables](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-tables-to-a-share), [views](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-views-to-a-share), [volumes](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-volumes-to-a-share), [models](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-models-to-a-share), and [notebooks](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-notebook-files-to-a-share).

- Use the open Delta Sharing protocol for sharing data with partners.
	[Delta Sharing](https://docs.databricks.com/aws/en/delta-sharing/) provides an [open solution for securely sharing live data](https://docs.databricks.com/aws/en/delta-sharing/share-data-open) from your lakehouse to any computing platform. Recipients do not need to be on the Databricks platform, on the same cloud, or on any cloud at all. Delta Sharing natively integrates with Unity Catalog, enabling organizations to centrally manage and audit shared data and AI assets across the enterprise and confidently share data and AI assets that meet security and compliance requirements.
	Data providers can share live data and AI models from where they are stored in the data platform without replicating or moving it to another system. This approach reduces the operational costs of data and AI sharing because data providers don't have to replicate data multiple times across clouds, geographies, or data platforms to each of their data consumers.
- Use Databricks-to-Databricks Delta Sharing between Databricks users.
	If you want to share data with users who don't have access to your Unity Catalog metastore, you can use [Databricks-to-Databricks Delta Sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks), as long as the recipients have access to a Databricks workspace that is enabled for Unity Catalog. Databricks-to-Databricks sharing allows you to share data with users in other Databricks accounts, across cloud regions, and across cloud providers. It's a great way to securely share data across different Unity Catalog metastores in your own Databricks account.

Like using an open source data format, using open standards for your AI workflows has similar benefits in terms of flexibility, agility, cost, and security.

[MLflow](https://mlflow.org/) is an open source platform for managing the ML and AI lifecycle. Databricks offers a fully managed and hosted version of MLflow, integrated with enterprise security features, high availability, and other Databricks workspace features such as experiment and run management and notebook revision tracking.

The primary components are [experimentation tracking](https://docs.databricks.com/aws/en/mlflow/tracking) to automatically log and track ML and deep learning models, [models](https://mlflow.org/docs/latest/models.html) as a standard format for packaging machine learning models, a [model registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) integrated with Unity Catalog, and the scalable, enterprise-grade [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

## 3\. Simplify new use case implementation

### Provide a self-service experience across the platform

There are several benefits of a platform where users have autonomy to use the tools and capabilities depending on their needs. Investing in creating a self-service platform makes it easy to scale to serve more users and drives greater efficiency by minimizing the need for human involvement to provision users, resolve issues, and process access requests.

The Databricks Data Intelligence Platform has all the capabilities needed to provide a self-service experience. While there may be a mandatory approval step, the best practice is to fully automate the setup when a business unit requests access to the lakehouse. Automatically provision their new environment, synchronize users and use SSO for authentication, provide access control to shared data and separate object stores for their own data, and so on. Together with a central data catalog of semantically consistent and business-ready data sets, new business units can quickly and securely access lakehouse capabilities and the data they need.

### Use serverless compute

For [serverless compute](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#serverless) on the Databricks platform, the compute layer runs in the customer's Databricks account. Cloud administrators no longer need to manage complex cloud environments that require adjusting quotas, creating and maintaining network resources, and connecting to billing sources. Users benefit from near-zero cluster startup latency and improved query concurrency.

### Use predefined compute templates

Predefined templates help control how compute resources can be used or created by users: Limit user cluster creation to prescribed settings or a certain number, simplify the user interface, or control costs by limiting the maximum cost per cluster.

The Data Intelligence Platform accomplishes this in two ways:

- Provide shared clusters as immediate environments for users. On these clusters, use autoscaling down to a very minimal number of nodes to avoid high idle costs.
- For a standardized environment, use [compute policies](https://docs.databricks.com/aws/en/lakehouse-architecture/operational-excellence/best-practices#standardize-compute-configurations) to restrict cluster size or features or to define t-shirt-sized clusters (S, M, L).

### Use AI capabilities to increase productivity

In addition to increasing productivity, AI tools can also help identify patterns in errors and provide additional insights based on the input. Overall, incorporating these tools into the development process can greatly reduce errors and facilitate decision-making - leading to faster time to release.

Databricks IQ, the AI-powered knowledge engine, is at the heart of the Data Intelligence Platform. It leverages Unity Catalog metadata to understand your tables, columns, descriptions, and popular data assets across your organization to deliver personalized answers. It enables several features that improve productivity when working with the platform, such as:

- [Databricks Assistant](https://docs.databricks.com/aws/en/notebooks/use-databricks-assistant) lets you query data through a conversational interface, making you more productive in Databricks. Describe your task in English and let the wizard generate SQL queries, explain complex code, and automatically fix errors.
- [AI-generated comments](https://docs.databricks.com/aws/en/comments/ai-comments) for any table or table column managed by Unity Catalog speed up the metadata management process. However, AI models are not always accurate and comments must be reviewed before saving. Databricks strongly recommends human review of AI-generated comments to check for inaccuracies.

## 4\. Ensure data consistency and usability

### Offer reusable data-as-products that the business can trust

Organizations seeking to become AI- and data-driven often need to provide their internal teams with high-quality, trustworthy data. One approach to prioritizing quality and usability is to apply product thinking to your published data assets by creating well-defined “data products”. Building such data products ensures that organizations establish standards and a trusted foundation of business truth for their data and AI goals. Data products ultimately deliver value when users and applications have the right data, at the right time, with the right quality, in the right format. While this value has traditionally been realized in the form of more efficient operations through lower costs, faster processes, and reduced risk, modern data products can also pave the way for new value-added offerings and data sharing opportunities within an organization's industry or partner ecosystem.

See the blog post [Building High-Quality and Trusted Data Products with Databricks](https://www.databricks.com/blog/building-high-quality-and-trusted-data-products-databricks).

### Publish data products semantically consistent across the enterprise

A data lake typically contains data from multiple source systems. These systems may have different names for the same concept (e.g., *customer* vs. *account*) or use the same identifier to refer to different concepts. So that business users can easily combine these data sets in a meaningful way, the data must be made homogeneous across all sources to be semantically consistent. In addition, for some data to be valuable for analysis, internal business rules, such as revenue recognition, must be applied correctly. To ensure that all users are using the correctly interpreted data, datasets with these rules must be made available and published to Unity Catalog. Access to the source data must be restricted to teams that understand the correct usage.

### Provide a central catalog for discovery and lineage

A central catalog for discovery and lineage helps data consumers access data from multiple sources across the enterprise, thus reducing operational overhead for the central governance team.

In Unity Catalog, administrators and data stewards manage users and their access to data *centrally across all workspaces* in a Databricks account. Users in different workspaces can share the same data and, depending on the user privileges centrally granted in Unity Catalog, can access data together.

For data discovery, the Unity Catalog supports users with capabilities such as:

- [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/) is the primary user interface for many Unity Catalog features. You can use Catalog Explorer to view schema details, preview sample data, and view table details and properties. Administrators can view and change owners, and administrators and data object owners can grant and revoke permissions. You can also use Databricks Search, which enables users to easily and seamlessly find data assets (such as tables, columns, views, dashboards, models, and so on). Users are shown results that are relevant to their search requests and that they have access to.
- [Data lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) across all queries run on a Databricks cluster or SQL warehouse. Lineage is supported for all languages and is captured down to the column level. Lineage data includes notebooks, jobs, and dashboards related to the query. Lineage can be visualized in Catalog Explorer in near real-time and retrieved with the Databricks REST API.

To allow enterprises to provide their users a holistic view of all data across all data platforms, Unity Catalog provides integration with enterprise data catalogs (sometimes referred to as the “catalog of catalogs”).