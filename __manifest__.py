{
   
 'name': 'Skill Swap Platform',
   
 'version': '1.0',
  
  'summary': 'A platform to allow users to swap skills with each other',
 
   'description': '''
       
          This module allows users to create skill profiles and exchange skills via swap requests.
  
         It includes user roles, access control, and basic view configurations.
 
   ''',
	
         'author': 'Team SkillSwap',

   	 'category': 'Social',
 
	 'depends': ['base'],
    
	'data': [
        'security/security.xml',
        
	'security/ir.model.access.csv',
        
	'views/skill_views.xml',
        
	'views/swap_views.xml',
    
	],
    
	'installable': True,
    
	'application': True,
    
	'license': 'LGPL-3',

}
