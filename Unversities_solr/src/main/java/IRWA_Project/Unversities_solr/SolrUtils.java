package IRWA_Project.Unversities_solr;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.solr.common.SolrInputDocument;

import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import net.minidev.json.JSONValue;

public class SolrUtils {

	private static final String SOLR_OPERATION_ADD = "add";

	private static final String SOLR_OPERATION_SET = "set";

	public static SolrInputDocument getSolrMetaDocumentfromFile(File file) throws FileNotFoundException, ParseException {
		JSONObject bookJson = (JSONObject) JSONValue.parse(new FileInputStream(file));
		return getSolrDocumentfromJson(bookJson);
	}

	

	

	public static SolrInputDocument getSolrDocumentfromJson(JSONObject json) throws ParseException {
		SolrInputDocument solrDocument = new SolrInputDocument();
		solrDocument.addField(SearchEngineCore.id, (String) json.get(SearchEngineCore.id));
		solrDocument.addField(SearchEngineCore.FacultyName, (String) json.get(SearchEngineCore.FacultyName));
		solrDocument.addField(SearchEngineCore.Type, (String) json.get(SearchEngineCore.ProgramName));
		solrDocument.addField(SearchEngineCore.ProgramName, (String) json.get(SearchEngineCore.ProgramName));
		solrDocument.addField(SearchEngineCore.ProgramUrl, (String) json.get(SearchEngineCore.ProgramUrl));
	

		return solrDocument;
	}

	
}
