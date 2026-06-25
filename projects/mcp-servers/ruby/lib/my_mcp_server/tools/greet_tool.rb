# frozen_string_literal: true

module MyMcpServer
  module Tools
    # A simple greeting tool.
    class GreetTool
      def self.name
        'greet'
      end

      def self.description
        'Greet a person by name with an optional title.'
      end

      def self.schema
        {
          type: 'object',
          properties: {
            name: {
              type: 'string',
              description: 'The name of the person to greet'
            },
            title: {
              type: 'string',
              description: 'Optional title (e.g. Mr., Ms., Dr.)'
            }
          },
          required: ['name']
        }
      end

      def self.execute(args)
        name = args['name']
        title = args['title']

        greeting = +'Hello'
        greeting << " #{title}" if title && !title.empty?
        greeting << ", #{name}!"

        { greeting: greeting }
      end
    end
  end
end
