# subman
Subscription management app written in Django

## Pricing
The application enables each module and add-on to have base pricing. The pricing can optionally have a tier specified. The tier of the account plan will be used to determine which pricing to use.

## Subscription plan lifecycle
A subscription plan has a start date and an end date. If no end date is specified, the plan will run until manually terminated. 

## Renewal
When a Plan comes up for renewal, the pricing can optionally be updated to the latest base pricing for the relevant modules and add-ons. Discounts and pricing overrides can also be updated.

## Logging
Expects a setting variable called SYSTEM_NAME which will be prepended in logging statements.

## Todo
- Pricing configuration should only have a module or an addon, not both.
- Filter list of available add ons in add on configuration
- Add one-off pricing type