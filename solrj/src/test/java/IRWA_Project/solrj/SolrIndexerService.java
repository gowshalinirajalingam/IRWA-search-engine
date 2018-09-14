package IRWA_Project.solrj;


import org.apache.solr.client.solrj.SolrServer;
import org.apache.solr.client.solrj.SolrServerException;
import org.apache.solr.client.solrj.impl.CommonsHttpSolrServer;
import org.apache.solr.common.SolrInputDocument;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
 
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Scanner;

public class SolrIndexerService {

	 private static final Logger log = LoggerFactory.getLogger(SolrIndexerService.class);
	 
	    private static final String SOLR_URL = "http://localhost:8983/solr/#/~cores/Universities";
	    private static final String FILE_PATH = "C:\\Users\\pavit\\Desktop\\ir_project\\docs\\C_horizon1.csv";
	 
	    public void indexFile() throws IOException, SolrServerException {
	        SolrServer server = new CommonsHttpSolrServer(SOLR_URL);
	        Scanner sc = new Scanner(new File(FILE_PATH));
	 
	        ProductBean bean;
	        String record;
	        String[] columns;
	        int recordCount = 0;
	        long currentTstmp = System.currentTimeMillis();
	 
	        while(sc.hasNextLine()) {
	            record = sc.nextLine();
	            if(record==null || record.length()<1){
	                continue;
	            }
	 
	            System.out.println(record);
	            columns = record.split(",");
	 
	            bean =
	                    new ProductBean(
	                            columns[0],
	                            columns[1],
	                           columns[2],
	                            columns[3],
	                            columns[4]);
	 
	            server.addBean(bean);
	            recordCount++;
	            if(recordCount%1000==0) server.commit();  // periodically flush
	        }
	 
	        server.commit();
	 
	        /* Remove all records with updated time less than current updated timestamp */
	        server.deleteByQuery("-last_updated:"+ String.valueOf(currentTstmp));
	        server.commit();
	 
	        server.optimize();
	        System.out.println("Done !!");
	    }
	 
	    public static void main(String[] args) throws IOException, SolrServerException {
	        new SolrIndexerService().indexFile();
	    }
}
