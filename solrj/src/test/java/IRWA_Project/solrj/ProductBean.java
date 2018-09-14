package IRWA_Project.solrj;
import org.apache.solr.client.solrj.beans.Field;

public class ProductBean {
	
	@Field("id")
	public  String id;
	
	@Field("FacultyName")
	public  String FacultyName;
	
	@Field("Type")
	public  String Type ;
	
	@Field("ProgramName")
	public  String ProgramName;
	
	@Field("ProgramUrl")
	public  String ProgramUrl;

	public ProductBean(){}
	
	public ProductBean(String id, String facultyName, String type, String programName, String programUrl) {
		this.id = id;
		this.FacultyName = facultyName;
		this.Type = type;
		this.ProgramName = programName;
		this.ProgramUrl = programUrl;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getFacultyName() {
		return FacultyName;
	}

	public void setFacultyName(String facultyName) {
		FacultyName = facultyName;
	}

	public String getType() {
		return Type;
	}

	public void setType(String type) {
		Type = type;
	}

	public String getProgramName() {
		return ProgramName;
	}

	public void setProgramName(String programName) {
		ProgramName = programName;
	}

	public String getProgramUrl() {
		return ProgramUrl;
	}

	public void setProgramUrl(String programUrl) {
		ProgramUrl = programUrl;
	}
	
	
	
	
	
	
}
