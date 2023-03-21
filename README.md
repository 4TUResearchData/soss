# Scientific open source Software (SOSS)

[![Project Status: WIP: Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

A repository that given an software arfefact DOI, it will computationally reproduce the software environment of the package.

## Description

This project aims to: (1) extract and link scientific software metadata from package files in a RDF KG and (2) recreate the software artefacts to compare with FAIR Maturity Evaluation services.

## Overview of the methodology: 

From a collection of software projects on 4TU, it produces reproducible sets of software artefacts and compare with FAIR evaluator

```mermaid
graph LR
A[Collect software artefacts] -->B(Identify single-software artefacts)
    B --> C{Processes}
    C -->|data collection| D[list of software artefacts API] --> Z(inspect source code e.g py file, readme for metadata extraction) --> F(GUIX package definition RDF) --> G(RDF/validation output)
    C -->|verify reproducible worflow| E[inputs software source code] --> H(build computational executable) --> J(JSON output)
    C -->|FAIR calculator| J(JSON output)
```

## Expected contributions


* 1. Add descriptors on existing RDF data model (reusing existing ontologies)
* 2. A framework to generate the dataset in RDF. It includes scripts for the collection of data and execution of the FAIR tests discrepancies in a sandbox environment
* 3. Raw data files from the dataset generation that can be reused for futher researcher


## Materials and resources

#### Available software repositories [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
A list of research software registries (also known as catalog, index, warehouse, repository, hub, platform, and other terms) can be found here: [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries) 

* [Research software directory]()
* [4TUResearchData repository]()
* [TUD]()
* [Research Software Heritage]()
* [Marven Central Repository]()
* [Apache projects](https://projects.apache.org/)
* [ORKG](https://orkg.org)
* [Codewithpapers](https://paperswithcode.com/)


#### Available ontologies

Concepts and properties are annotated with:
* [GUIX Package difinitions](https://guix.gnu.org/manual/en/html_node/Defining-Packages.html)
* [Semanticscience Integrated Ontology (SIO)](https://bioportal.bioontology.org/ontologies/SIO/)
* [Software Ontology (SWO)](https://www.ebi.ac.uk/ols/ontologies/swo)
* [Research Software Ontology (RO)](https://wf4ever.github.io/)
* Ontology of Software Depencencies (OSD)
* [OKG-Soft](https://ieeexplore.ieee.org/document/9041835)
* [ML Schedma Core Specification](http://ml-schema.github.io/documentation/ML%20Schema.html)

#### Data Model
Explaining the elements of a knowledge graph for the research software artefacts:
* Source code repo: entity that host +1 packages/module
* Package: a sub-module that provides a reusable piece of software
* Version: a tag associated with a repo or package that identifies the unique instance or release of the source
* djht:software: a computational related flaw associated with versions of a repo or package 
<!-- has version: a one-to-many relationship between package and version
has STAR: a one-to-many relationship between version and STAR
has fixed version: (if any) a one-to-many relationship between STAR and fixed version
has dependency:
has transitive dependency -->
```mermaid
graph TD
   A((Repo)) -->|rdf:has dependecy| B((ml: version))
   A((Repo)) -->|ml: has transitive dependency| B
   C((ml: package)) -->|ml: has version| B
   B -->|has software| D((djht: software))
   D -->|fixed version| B
   D --> |djht: has author| E((ORCID))
   D --> |has source| F((Source Code))
   D --> |has categories| G((Tags))
   D --> |has files| H((djht:files))
```

#### Example RDF (turtle):

```ttl
# metamodel_version: 1.7.0
@prefix djht: <http://djht.org/ontology/djht/> .
@prefix mls: <http://www.w3.org/ns/mls#> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://doi.org/10.4121/19145426.v1> a mls:Software ;
    djht:authors "0000-0002-9994-1462, 0000-0002-9994-XXXXX" ;
    djht:files 8 ;
    djht:funding "EU-horizon" ;
    djht:tags "data science" ;
    schema:name "Characterizing single-molecule dynamics of viral RNA-dependent RNA polymerases with a multiplexed magnetic tweezers" ;
    mls:function "1-800" .

<https://doi.org/10.4121/19145426.v2> a mls:Software ;
    djht:dependencies 90 ;
    djht:funding "none" ;
    djht:references "none" ;
    djht:tags "AI" ;
    schema:name "Characterizing single-molecule dynamics of viral RNA-dependent RNA polymerases with a multiplexed magnetic tweezers" ;
    mls:function "1-800" .

[] a djht:Container ;
    djht:softwares <https://doi.org/10.4121/19145426.v1>,
        <https://doi.org/10.4121/19145426.v2> .
```
---
## License

**Copyright (C) 2023 - MIT License**



---
