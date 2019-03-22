/*
 * To change this template, choose Tools | Templates and open the template in
 * the editor.
 */
package checkresult;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;
import org.openscience.cdk.DefaultChemObjectBuilder;
import org.openscience.cdk.exception.CDKException;
import org.openscience.cdk.interfaces.IAtomContainer;
import org.openscience.cdk.io.iterator.DefaultIteratingChemObjectReader;
import org.openscience.cdk.io.iterator.IteratingMDLReader;
import org.openscience.cdk.io.setting.IOSetting;
import org.openscience.cdk.tools.manipulator.AtomContainerManipulator;

/**
 *
 * @author cesar
 */
public class ComputeRotableAndDihedralAngles 
{
    public static void main( String[] args ) throws Exception
    {
        File root = new File( System.getProperty( "user.dir" ) );
        File[] files = root.listFiles( (File dir, String name) ->
        {
            return name.toLowerCase().endsWith( ".sdf" );
            
        });
        
        RotatableBondsCountDescriptor a = new RotatableBondsCountDescriptor();
        
        for ( File molFile : files )
        {
            Scanner read = new Scanner( new FileInputStream( molFile.getName().substring( 0, molFile.getName().lastIndexOf( ".sdf" ) ) + ".pdb" ) );
            List<String> atomFromPDB = new ArrayList<>();
            while ( read.hasNext() )
            {
                String line = read.nextLine();
                if ( line.toLowerCase().startsWith( "atom" ) )
                {
                    StringTokenizer token = new StringTokenizer( line, " " );
                    token.nextToken();
                    token.nextToken();
                    atomFromPDB.add( token.nextToken() );
                }
            }
            
            DefaultIteratingChemObjectReader reader = getInputStreamSDFReader( molFile );
            Writer writer = new BufferedWriter( new FileWriter( new File( molFile.getName() + ".txt" ) ) );    
            
            IAtomContainer molecule = (IAtomContainer) reader.next();            
            AtomContainerManipulator.percieveAtomTypesAndConfigureAtoms( molecule );
            
            a.calculate1( molecule, writer, atomFromPDB );
            
            reader.close();
            writer.flush();
            writer.close();
        }
    }
    
    static private DefaultIteratingChemObjectReader getInputStreamSDFReader( File file ) throws FileNotFoundException
    {
        FileInputStream fis = new FileInputStream( file );
        DefaultIteratingChemObjectReader iterReader = new IteratingMDLReader( fis, DefaultChemObjectBuilder.getInstance() );
        iterReader.addChemObjectIOListener( ( IOSetting setting ) ->
        {
            if ( "ForceReadAs3DCoordinates".equals( setting.getName() ) )
            {
                try 
                {
                    setting.setSetting( "true" );
                }
                catch ( CDKException e )
                {
                }
            }
        });
        
        if ( iterReader instanceof IteratingMDLReader )
        {
            ((IteratingMDLReader) iterReader).customizeJob();
        }
        
        return iterReader;
    }
}
