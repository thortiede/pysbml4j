# pysbml4j.AnalysisApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gene_analysis**](AnalysisApi.md#get_gene_analysis) | **GET** /geneAnalysis | Relation- and Pathway Analysis for a gene
[**get_gene_set**](AnalysisApi.md#get_gene_set) | **GET** /geneSet | provide a list of genes and get a network containing all genes and their respective relations
[**get_gene_set_analysis**](AnalysisApi.md#get_gene_set_analysis) | **POST** /geneSetAnalysis | Relation- and Pathway Analysis for a set of genes

# **get_gene_analysis**
> list[GeneAnalysisItem] get_gene_analysis(gene_symbol)

Relation- and Pathway Analysis for a gene

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.AnalysisApi()
gene_symbol = 'gene_symbol_example' # str | The geneSymbol for which the analysis should be fetched

try:
    # Relation- and Pathway Analysis for a gene
    api_response = api_instance.get_gene_analysis(gene_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_gene_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_symbol** | **str**| The geneSymbol for which the analysis should be fetched | 

### Return type

[**list[GeneAnalysisItem]**](GeneAnalysisItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_set**
> str get_gene_set(user, gene_symbols, uuid=uuid, directed=directed)

provide a list of genes and get a network containing all genes and their respective relations

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.AnalysisApi()
user = 'user_example' # str | The user which requests the creation
gene_symbols = ['gene_symbols_example'] # list[str] | The geneSymbols for which the analysis should be fetched
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the parent network to derive a new network from, if omitted the full model will be used (optional)
directed = false # bool | Boolean flag wether the resulting network-graph should be directed  (optional) (default to false)

try:
    # provide a list of genes and get a network containing all genes and their respective relations
    api_response = api_instance.get_gene_set(user, gene_symbols, uuid=uuid, directed=directed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_gene_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **gene_symbols** | [**list[str]**](str.md)| The geneSymbols for which the analysis should be fetched | 
 **uuid** | [**str**](.md)| The UUID of the parent network to derive a new network from, if omitted the full model will be used | [optional] 
 **directed** | **bool**| Boolean flag wether the resulting network-graph should be directed  | [optional] [default to false]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_set_analysis**
> list[GeneAnalysisItem] get_gene_set_analysis(body)

Relation- and Pathway Analysis for a set of genes

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.AnalysisApi()
body = ['body_example'] # list[str] | A json formatted and comma separated list of genes in the set to be analysed


try:
    # Relation- and Pathway Analysis for a set of genes
    api_response = api_instance.get_gene_set_analysis(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_gene_set_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| A json formatted and comma separated list of genes in the set to be analysed
 | 

### Return type

[**list[GeneAnalysisItem]**](GeneAnalysisItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

