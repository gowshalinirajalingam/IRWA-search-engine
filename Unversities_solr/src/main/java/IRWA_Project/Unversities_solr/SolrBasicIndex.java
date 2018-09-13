package IRWA_Project.Unversities_solr;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;

import org.apache.solr.client.solrj.SolrClient;
import org.apache.solr.client.solrj.SolrQuery;
import org.apache.solr.client.solrj.SolrServerException;
import org.apache.solr.client.solrj.beans.DocumentObjectBinder;
import org.apache.solr.client.solrj.impl.HttpSolrClient;
import org.apache.solr.client.solrj.response.QueryResponse;
import org.apache.solr.client.solrj.response.UpdateResponse;
import org.apache.solr.common.SolrDocument;
import org.apache.solr.common.SolrDocumentList;
import org.apache.solr.common.SolrInputDocument;
import org.apache.solr.common.params.CommonParams;



public class SolrBasicIndex {

	private static File solrJsonDirectory = new File("C:\\Users\\pavit\\Desktop\\ir_project\\docs\\test");

	private static SolrClient client = null;

	public static void main(String[] args) throws SolrServerException, IOException, ParseException {
		client = new HttpSolrClient.Builder("http://localhost:8983/solr/Universities").build();
		 index();
		
		//Then create the Query
			SolrQuery query = basicQuery("59");
			System.out.println("Query formed as "+query.toQueryString());
			
			//Then execute the query and get the Document list that match the query
			SolrDocumentList documentList = executeQuery(query);
			
			
			//At last print the returned documents
			printAsDocuments(documentList);
		

	}
	
	private static void index() throws SolrServerException, IOException, ParseException {
		for (File file : solrJsonDirectory.listFiles()) {
			System.out.println("Indexing " + file.getName());
			SolrInputDocument solrDocument = SolrUtils.getSolrMetaDocumentfromFile(file);
			client.add(solrDocument);
		}

		client.commit();
	}
	
	private static SolrQuery basicQuery(String id) {
		//Build the query
		
		StringBuffer buffer = new StringBuffer();
		buffer.append(SearchEngineCore.id).append(":").append(id);
		
		SolrQuery query = new SolrQuery();
		query.set(CommonParams.Q, buffer.toString());
		
		return query;
	}
	
	private static SolrDocumentList executeQuery(SolrQuery query) throws SolrServerException, IOException {
		
		//Limit the output
		query.setRows(10);
		//Execute the query and catch to a QueryResponse
		QueryResponse response = client.query(query);
		
		SolrDocumentList result	 = response.getResults();
		System.out.println("No of document returened : "+result.getNumFound());
		
		return result;
	}
	
	private static void printAsDocuments(SolrDocumentList documentList) {
		
		for(SolrDocument document : documentList) {
			Object object = document.get(SearchEngineCore.id);
			System.out.println("id value is : "+object);
		}
		
	}
}
