---
type: web clipped
status: raw
tags:
capture_date: 2025-11-12
url: https://medium.com/@piethein/unstructured-data-management-at-scale-4c612f822f70
relevance to: "[["
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Mastodon](https://me.dm/@piethein)

Over the years, I have collaborated with many enterprises, and one constant challenge has emerged: managing unstructured data at scale. Yet a comprehensive set of best practices is missing. The public domain surrounding this critical subject is limited, leaving many organizations puzzled with the complexities of unstructured data. Today, as we stand on the new era with Generative AI, the urgency to address these challenges has never been greater.

In this blog post, I will explore potential solutions and best practices to help organizations navigate the complexities of unstructured data effectively.

### Background context — Medallion design pattern

In navigating the complexities of unstructured data management, I’ve found inspiration in the Medallion Architecture framework. This model’s metaphor of “communication through layers” beautifully encapsulates a fundamental truth: the real work lies not merely in transforming or reworking data, but in translating its meaning across various boundaries. The Medallion design pattern serves not just as a data framework but as a lens through which we can communicate and comprehend complexity. Moreover, the layering itself acts as a communication pattern, facilitating clearer interactions and understanding among stakeholders.

As we delve deeper into the complexities of managing unstructured data, it is essential to quickly introduce the Medallion Architecture — a framework traditionally centered around structured data organized into three distinct layers: Bronze, Silver, and Gold. The Bronze layer serves as the raw data repository, where data is ingested and stored in its original form. The Silver layer focuses on refining this data, applying transformations and cleansing processes to enhance its quality. Finally, the Gold layer represents the most refined and curated data, ready for analysis and decision-making.

However, with the increasing widespread need of using unstructured data for Generative AI, it is clear that the Medallion Architecture must evolve. The challenge now lies in accommodating unstructured data within this framework to enable AI application readiness.

This blogpost addresses two pivotal questions: 1) Is it practical to have a unified layered architecture for managing structured, semi-structured, and unstructured data? 2) Additionally, how can large language models (LLMs) be integrated into the existing processes associated with the Medallion framework?

Let me lay my cards on the table: I firmly believe that managing structured and unstructured data holistically holds immense value, paving the way for more comprehensive and effective data- and AI-driven insights. Furthermore, LLMs are transforming data management tasks such as cleansing and integration, prompting a reimagining of traditional paradigms. This creates a synergy that brings together generative AI development, data engineering, and document management into a unified architecture.

To delve deeper into this transformation, we will begin with an overview of the challenges and opportunities presented by unstructured data in modern AI contexts, highlighting the role of the retrieval-augmented generation (RAG) pattern in using such data effectively. Following this, we will outline the specifics of each layer in the Medallion architecture as it relates to unstructured data management, detailing processes from data collection and cleaning to advanced refinement and indexing for AI-driven searches and applications.

Furthermore, the blogpost will discuss the synergistic potential of integrating LLMs within the Medallion architecture, illustrating through practical scenarios how these models enhance data transformation, cleaning, and enrichment processes. By the end of this blogpost, you will not only have gained knowledge to implement or enhance the Medallion architecture within your own AI and data management strategies.

## Unstructured Data Processing

In today’s landscape, the Medallion architecture has been predominantly focused on structured data, which is well-organized and easily searchable by using open table formats, such as Delta Lake or Iceberg. This structured approach facilitates straightforward processing and analysis but fails to address the complexities of managing the unstructured data that modern systems frequently require.

LLMs primarily engage with content that is stored in semi-structured and unstructured data formats, encompassing diverse forms like JSON and XML files as well as PDF and Word documents, emails, social media content, or speech and images. These data types, characterized by their richness and complexity, requires robust and flexible architectures to be managed effectively. To address this need, let’s start by examining the RAG pattern, a key framework for LLMs to work with unstructured data. After that, we’ll delve into managing unstructured data and its alignment with the RAG pattern. Then, finally, we will draw conclusions and move on to the layering.

### Retrieval-Augmented Generation

RAG is a crucial framework in the realm of generating more precise and relevant responses with modern AI and LLMs. The RAG pattern, which is visualized in the image below, is a method that enhances language model outputs by incorporating external knowledge.

Thus, instead of relying solely on the foundational model’s source knowledge, RAG allows you to provide additional context to the model, enabling it to generate more precise and relevant responses. To implement RAG, the process begins by gathering data relevant to a particular use case and dividing it into smaller, manageable pieces, or chunks. These chunks are then transformed into vector embeddings, which are numerical representations designed to capture semantic meanings. In this setup, shorter distances between vectors signify a higher degree of similarity. The numerical formats and content are subsequently stored in a vector database.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*7-MlRqHNwgtfilJINlALMw.png)

The RAG pattern (Source: Building Medallion Architectures by Piethein Strengholt)

Once the vector database is populated, the RAG system enhances its effectiveness by augmenting the initial prompt with supplementary content.

Here’s how it works in more detail: when a user or an application inputs a prompt (step 1 in the figure), this prompt is transformed (step 2) into a vector using the same embedding model previously employed to populate the database. Using this embedded prompt, the system retrieves (step 3) the vectors closest to it from the database, which represent the most pertinent information. This content is then integrated (step 4) with the original prompt and processed by an LLM to generate a response that is both contextually richer and more precise.

To maximize the effectiveness of the RAG pattern, it’s essential to ensure the data is well-structured and organized. Here are some typical steps involved:

1. **Capture the raw documents:** Extract data from both structured and unstructured sources, categorizing them by source, date, or business process.
2. **Generate document metadata:** Generate and extract metadata such as creation date, document titles, page numbers, URLs, or other relevant information.
3. **Organize and standardize documents:** Rearrange the documents in a structured manner using a standard format. Standardizing documents during this process ensures high reusability.
4. **Chunk documents:** Break down the documents into smaller, more manageable parts for efficient processing by the LLM.
5. **Embed chunks:** An embedding model transforms each chunk into numeric vectors.
6. **Index chunks in a vector database:** Load the vector representations of the chunks, along with the chunk’s text, into a vector database.

To effectively manage and leverage the potential of unstructured data within AI systems, it is essential to align architectural layers. Here, we have already outlined the Medallion architecture, consisting of three critical layers: Bronze, Silver, and Gold, each designed to progressively refine the data. Let’s explore how these layers align with the RAG pattern to optimize data handling and LLM integration. We will discuss one layer at a time, and after that, we will draw conclusions.

## Bronze Layer

The Bronze layer marks the initial stage in the unstructured data stack, with a stark focus on data extraction and ingestion. In this setup, the Bronze layer serves the same purpose as it does for capturing and organizing structured data. In the context of unstructured data, the focus is on capturing, extracting, and optimizing raw data for storage and processing. This foundational layer is essential for collecting unstructured data from various sources, such as log files, social media platforms, customer feedback forms, emails, and scientific research documents.

To extract unstructured data, organizations typically use techniques such as upload forms, web scrapers, API integration, file parsers, and copying jobs. Depending on the types of data and the accuracy needed, they may either develop custom extractors or utilize pre-built ones, such as [LlamaParse](https://github.com/run-llama/llama_parse) and [Tensorlake](https://github.com/tensorlakeai) to ensure high accuracy rates in data extraction. These extractors are also useful in the Silver and Gold layers, where they allow customization with parsing rules and patterns to better suit specific data extraction needs. We’ll come back to this point in the next sections.

After extracting the data, organizations transfer data in its original file format, such as PDF, DOCX, or TIFF, to a raw data storage system, often a object storage service like [Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) or [Amazon S3](https://aws.amazon.com/s3/). During this transfer, additional metadata is often generated to provide more context about the data, such as its source, its format, the person or process that uploaded the document, the creation date, and so on. This metadata is usually stored in a data catalog or alongside the unstructured data, ensuring a clear record of the data’s origin and history.

To generate metadata, organizations can use small language models (SLMs). These models are more efficient and optimized for specific tasks compared to their larger counterparts. SLMs excel in classifying, labeling, identifying sensitive and Personally Identifiable Information (PII), performing entity extraction, and summarizing, making them ideal for handling metadata generation efficiently. The metadata generated by SLMs is crucial for the subsequent layers of the Medallion architecture, as it provides context and additional information about the unstructured data. It’s also expected that this metadata is passed forward to the subsequent layers. For example, sensitive data or PII labels generated by SLMs in the Bronze layer can be used to enforce data access policies in the Silver and Gold layers.

> SLMs are also highly effective for generating metadata for structured data. Aligning the management of both unstructured and structured data is considered a best practice, enhancing consistency and coherence across data systems. To effectively scale and manage this metadata, invest in a robust metastore or data fabric solution is essential.

Another objective for the Bronze stage is the initial sorting of data, setting the groundwork for later processing. This objective parallels the organization of structured data in the Bronze layer, where the primary goal is to preserve its raw form while maintaining accessibility. To organize the data, organizations often set up folders or containers that mirror business processes or data origins, such as Teams channels or SharePoint folders. This approach helps maintain order, making it easier to access and process data later. Furthermore, organizations frequently use a partitioning strategy, such as organizing by date, to implement time-based versioning for different documents. This method transforms unstructured data into an archive, much like the Bronze layer when it is used with structured data, preserving its raw form.

In this data lake structure, it’s essential to maintain strong links to the schema definitions, parsers, and extraction scripts. Concretely, in the Bronze layer, you organize by data source, project, or business process. Within each folder or container, there are subfolders for raw data, intermediate data, and metadata. Within this metadata, you maintain references to schema definitions (for semi-structured documents), parsers, and scripts, typically housed in a code repository. This arrangement allows you to trace every data piece back to its origin, ensuring you have all the necessary information for processing and analysis in later stages.

To conclude: the Bronze layer, in the context of unstructured data, is essential for capturing data in its most authentic and raw form, providing a detailed snapshot for further refinement. It is crucial to maintain clarity about the data’s origin throughout this process. For the effective identification and sorting of unstructured data, LLMs and SLMs can be used to generate metadata, adding a structured layer of information to the otherwise unstructured data. This metadata plays a critical role in the subsequent layers of processing.

## Silver Layer

Moving to the Silver layer, the emphasis shifts towards refining and stabilizing the data to make it functional for AI-driven use cases. An important aspect at this stage is ensuring the data’s reusability. This not only benefits RAG applications but also serves future fine-tuning models.

At this stage, it becomes essential to partition the previously raw data into logically organized units based on semantically meaningful contexts. This involves a detailed process of restructuring, labeling, and cleaning the data to ensure its consistency and usability. This also involves techniques such as noise detection and duplicate identification, which help filter out irrelevant or erroneous information that could compromise the accuracy of AI outputs. Note that LLMs are also instrumental in this phase, as they can help identify and correct errors in the data, ensuring that the information is accurate and reliable.

> Regarding the quality of unstructured data, it is highly subjective and can even be biased due to the collection process. Therefore, it is imperative for organizations to establish their own quality assessment frameworks. Consider utilizing an LLM as a judge to oversee this framework.

After the unstructured data has been checked for quality, cleaned, and partitioned, it is then often formatted into a structured, machine-readable format. Employing markup languages, particularly [Markdown](https://en.wikipedia.org/wiki/Markdown), is recognized as a best practice due to its lightweight and readable syntax. Using Markdown simplifies the documents, making them more programmatically accessible and easier to handle for AI systems, thereby enhancing their compatibility with various analytical tools and platforms. The simplicity of Markdown helps AI models to more effectively parse and comprehend the content, which is crucial for tasks such as information retrieval, classification, and summarization.

Frameworks like [MarkItDown](https://oreil.ly/pLnsJ) and [PyMuPDF](https://oreil.ly/OzrQ0) are instrumental at this stage because they standardize the output and prepare the data for more sophisticated analytical tools. The clean and clearly formatted data is then ready for deeper analysis and insights extraction. The straightforward nature of Markdown minimizes potential errors associated with complex formatting, ensuring the data remains pristine and consistent.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*AJir-kYi50XgoGMXIqRSyA.png)

There is a strong synergy between LLMs and the Medallion framework. As shown in pattern 1, LLMs and SLMs excel at extracting critical information from various formats, such as text intertwined with numerical data from logs, emails, or reports. They can also be used to enrich or transform content within the structured data processing chain. Conversely, the Medallion framework’s big data processing capabilities (pattern 2) allow for scalable document and chunk processing. Finally, feeding context (data) directly from the Medallion layers to Agents greatly enhances the implementation of AI applications, as illustrated in pattern 3.

During this data transformation phase, extra metadata is often generated to help AI systems better understand the context of the data. Key activities for the Silver layer include the following:

- Summarizing extensive documents concisely.
- Breaking down complex documents into smaller, more manageable parts. This may also involve extracting images and tables within the documents and storing them separately with references. Note that this process isn’t part of the chunking strategy, which is typically deferred to later stages when the unstructured documents are refined for specific AI applications.
- Translating different languages to the same organizational language for consistency (with the help of LLMs).
- Creating classifiers and labels for the sensitivity of the data. For example, you could apply a classification of “Confidential” based purely on content type, and assign a sensitivity label indicating “Low Risk” based on access controls or the potential impact of data exposure.
- Classifying and categorizing text.
- Recognizing and extracting entities, such as using an LLM to identify and organize critical information like party names, contract dates, and obligations into a structured database for quick reference.
- Modeling topics and analyzing trends.
- Handling sensitive data within documents by breaking up markup files into different parts, allowing for more fine-grained access and control.
- Storing the metadata in a structured format, such as a catalog or a metadata store, or alongside the unstructured data in the data lake.

To support these activities, selecting the appropriate data processing engines is crucial. These engines differ based on various factors, such as their design for structured or unstructured data and whether they operate on a single node or in a distributed environment. Additionally, the data stored in the Silver layer can be accessed by other upstream applications. For instance, a knowledge graph tool could tap into the entities and other metadata present in the Silver layer.

### Promoting Silver data into data products

Once unstructured data has been standardized and stabilized, I advocate for promoting them within a data marketplace. Such a marketplace serves as a centralized portal where stakeholders, such business users and value engineers, can discover and access AI-related information about various use cases, including agents and the unstructured or structured data they utilize. By facilitating easy access to these assets, organizations can drive innovation, enhance collaboration, and foster a culture of data sharing.

This approach holds immense value for several reasons. First, it democratizes access to high-quality data, enabling teams across the organization to leverage the insights derived from previously untapped resources. Second, it encourages cross-functional collaboration, allowing data scientists, engineers, and business analysts to explore new possibilities and develop innovative solutions that may not have been previously considered. Lastly, a data marketplace can stimulate a feedback loop, where users provide insights and suggestions, further improving the quality and relevance of the data assets available.

After reading this section, you might question: **“Why is the Silver layer used as input for data product creation? Why not the Gold layer? And isn’t this counterproductive, as the representations of documents and vectors for each model can change depending on the use case?”**

The answer lies in reusability versus the nature of operationalizing language models and training. Each use case depends on stable and predictable data to yield reliable outcomes, and the Silver layer serves a crucial purpose in this regard. It prepares data for the rapid deployment of new RAG applications and the fine-tuning of LLMs for specific tasks. It also reworks unstructured data found at the source, making it accessible for all future use cases.

This approach addresses the lack of a systematic method for onboarding and managing unstructured data (documents). Instead of repeatedly identifying documents and onboarding them for each use case and reworking their quality and structure, I propose an intermediate step of cleaning, metadata generation, and standardizing the documents using a common Markdown format and publishing them into a catalog as data products.

Consequently, specific chunking strategies and changes to the context will need to be deferred until the data is appropriately processed. Once this stabilization is achieved, the data becomes primed for further utilization in advanced AI applications in the Gold layer.

## Gold Layer

Transitioning to the Gold layer, the data refinement reaches a stage where it is tailored to meet the specific demands of particular applications. This layer focuses on enhancing the precision and specificity of the data to ensure it aligns perfectly with the intended use.

For teams leveraging unstructured data for applications like RAG, the process begins with selecting the most relevant documents or objects for the specific use case, based on specific criteria, such as keywords, topics, or entities. Again, you could draw a parallel to the structured data process, where generalized data is selected and refined for specific analytical use cases.

After selecting data, typically another data preprocessing step is included to enhance the data for the specifics of the use case. Techniques like data augmentation could make the data more representative, accurate, and diverse. This step is crucial for ensuring the data is well-suited for the intended application, such as training an LLM for a specific task or the embedding process. Again, language models could play a role in this step, as they can generate additional data points and context, or refine existing ones to enhance the dataset.

The next critical step involves chunking data and generating embeddings — this is where embedding models come into play to represent text as vector strings, encapsulating the semantic meanings of the data. This takes us back to the earlier conversation about the RAG pattern, where the data is transformed into numerical representations and stored within a vector database. It’s hard to generalize this process for all use cases because each application has its unique requirements, such as what data is required, the chunking strategy, and the choice of embedding model. While the tasks of chunking and embedding are distinct, they are interdependent:

- **Chunking strategy:** This approach involves breaking down large documents into smaller, manageable pieces, or “chunks,” before processing them with an embedding model. The strategy is crucial because embedding models often have a limit on the input size they can handle effectively. For example, in question-answering applications, documents are typically chunked into sizes like paragraphs, ensuring that each chunk contains enough context to answer potential questions. Furthermore, models have token limits, beyond which their performance may degrade, or they might not process the input at all. Therefore, chunking is essential to ensure that the data is processed effectively and accurately.
- **Embedding models:** Embedding models play a crucial role in transforming text into numerical representations that capture the semantic meaning of the content. The choice of an embedding model can affect how well the semantic relationships in your text are captured and preserved. Different models have varying capabilities in terms of capturing context, handling different languages, and encoding domain-specific knowledge. For example, a low-dimensional embedding model is tailored for efficiency and minimal resource consumption, making it suitable for real-time environments such as chatbots. On the other hand, a high-dimensional embed‐ ding model offers intricate representations ideal for tasks that demand thorough analysis and precision, such as detailed academic research. Therefore, it is crucial to choose an embedding model that aligns with the specific needs of your application.

To facilitate efficient retrieval of semantically correlated data by LLMs, it is imperative that the data is vectorized, stored, and indexed in a manner that allows for rapid and effective search capabilities. Choosing the right storage solutions, such as vector databases or data lakes, is crucial at this stage to manage the volume and variety of unstructured data effectively. In the Gold layer, the aim is to refine unstructured data into a form that is not only structured but also meticulously curated for specific applications. Consequently, the data transcends its original unstructured state to become highly targeted and fit for purpose.

Database engines like [Pinecone](https://www.pinecone.io/), [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) and [Mosaic AI Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search) are often employed to ensure that the data is not only accessible but also organized in a way that supports decision making processes and enhances AI applications. So, for the Medallion architecture, this effectively means the data is provided through a serving layer that is optimized for AI applications.

> Note that the design of the Silver and Gold layers come with nuances, influenced by factors like the size of the organization, the number of sources, semantic requirements, and specific consumer needs. Additionally, you can introduce layers or defer certain activities if necessary, as these layers should be viewed as logical constructs rather than physical ones.

Now that we have discussed all the layers, let’s transition to the governance aspect before drawing our final conclusions.

## Governance

Robust data governance is crucial for managing unstructured data across the different layers of the architecture. It’s essential to implement clear guidelines on how data can move from one layer to another or from one domain to another. For example, restrict data from the Bronze layer to its own domain; or only allow certified datasets from the Silver layer or data from the Gold layer to be shared externally. Let’s focus on the individual layers once more to better understand their specific roles and governance requirements.

In the Bronze layer, maintaining tight feedback loops with the sourcing application teams is essential. If issues with technical validation or ingestion arise, the providing teams responsible for the document management systems or applications must address these issues promptly. This ensures that data management remains efficient and secure throughout the process. Furthermore, ensure security measures are in place right from the point of data collection or ingestion. So, (automatically) label and classify data as soon as it enters the architecture. Optionally, symmetric encryption frameworks can be used to protect PII or other sensitive data. Therefore, it is crucial to define organization-wide sensitivity labels and classification schemas beforehand to ensure consistent protection of PII and other sensitive data.

Moving on to the Silver and Gold layers, your governance should prioritize integrity, consistency, and usability. Develop rules to standardize data: data formats, such as Markdown, image and video formats, naming conventions, required metadata, and so on. Such rules ensure uniformity across your processed unstructured data.

In the Silver layer, focus on maintaining the reusability of unstructured data without mixing documents between different contexts, allowing application teams to retain clear data ownership. Regular audits are essential to ensure compliance with governance standards, helping to uphold the quality and reliability of your data as it progresses through your architecture. As a final step, consider a sign-off and the publication of a data product, which serves as a logical entity that references the underlying data assets by providing links to the locations where the actual processed unstructured data is stored.

Moving to the Gold layer, prioritize selecting a design tailored to your use case’s needs, emphasizing the nuances of unstructured data. Here, implement specific chunking strategies to break down large volumes of data into manageable pieces, and utilize vector stores for efficient storage and retrieval. Additionally, managing the relationship to the catalog and incorporating semantic contextual information about the data and documents is essential. This extra discipline ensures that data is well-organized, easily discoverable, and contextually understood, further supporting effective data management.

Within the overall governance framework, it is important to add additional roles that correspond to key responsibilities. Data owners should align with document owners to maintain accountability for data quality and integrity. Context engineers will be responsible for producing high-quality content and contextual information to enhance reusability. Finally, value engineers will work closely with the consuming side of the architecture, where data is transformed into value with the help of AI. This comprehensive approach not only safeguards unstructured data but also enhances confidence in deploying AI applications across various departments or organizational units.

## Wrapping up

Having completed the unstructured data processing journey, we can confidently say that the prescriptive labels of the Medallion architecture can be effectively reused to manage the complexities of unstructured data.

By leveraging its layering, you can separate concerns in managing unstructured data. Moreover, utilizing LLMs to generate metadata enhances the management of both structured and unstructured data. Therefore, adopting a unified Medallion architecture for handling both types of data is advantageous, as it aligns diverse disciplines for improved outcomes.

Looking ahead, the role of context and value engineers will become increasingly vital. As the rise of context-aware protocols, such as the Model Context Protocol (MCP), introduces resources, tools, and tasks,the need for individuals who truly understand the business domain, its processes, and its context becomes paramount. These engineers will be responsible for reworking content, adding extra context, mapping complex business scenarios into resources, actions and tools, that enable agents to operate effectively.

In this new era of AI, the Medallion framework is designed to decouple concerns and establish clear boundaries that facilitate communication and collaboration among teams and members. By establishing these boundaries, the framework not only streamlines processes but also fosters an environment where context engineers can thrive, ensuring that the insights derived from both structured and unstructured data are effectively translated into actionable business functions. This synergy will ultimately lead to enhanced performance and more successful outcomes in AI-driven applications.

In closing, I would like to mention that much of the content presented here has been sourced from my new book, [*Building Medallion Architectures*](https://www.oreilly.com/library/view/building-medallion-architectures/9781098178826/). If you are interested in exploring these concepts in greater depth and learning more about effectively managing unstructured and structured data within the Medallion framework, I encourage you to read it.

Piethein Strengholt is a seasoned expert in data management with significant experience in chief data officer (CDO) and chief data architect roles.

## Responses (3)

Sitthichat Sukpholtham

What are your thoughts?  [Statswork](https://medium.com/@statswork?source=post_page---post_responses--4c612f822f70----0-----------------------------------)

[

Aug 1

](https://statswork.medium.com/really-enjoyed-this-breakdown-especially-the-part-about-ai-enabling-product-teams-to-anticipate-6012d71ab5b0?source=post_page---post_responses--4c612f822f70----0-----------------------------------)

```c
Really enjoyed this breakdown—especially the part about AI enabling product teams to anticipate user needs rather than just react to them. Your emphasis on data quality as a foundational pillar really resonated with me. At Statswork, we often help…
```

6

```c
Your analysis of managing unstructured data at scale correctly identifies the need for architectural solutions, but misses the core paradox: imposing macro-level structure inevitably creates micro-level chaos. Your proposed frameworks—data lakes…
```

5

```c
Thanks for writing this up! I am not sure if I would do it this way, but it's great to have a reference point.
```

2

## More from Piethein Strengholt

## Recommended from Medium

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--4c612f822f70---------------------------------------)